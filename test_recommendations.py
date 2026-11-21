import unittest

from recommendations import CATALOG, GENRES, recommend_titles, score_title


class RecommendationTests(unittest.TestCase):
    def test_questionnaire_covers_ten_genres(self) -> None:
        self.assertEqual(len(GENRES), 10)

    def test_recommendations_rank_titles_matching_favorite_genres(self) -> None:
        preferences = {genre: 3.0 for genre in GENRES}
        preferences["Ciencia ficción"] = 5.0

        recommendations = recommend_titles(preferences)
        scores = {title["title"]: float(title["score"]) for title in recommendations}

        self.assertTrue(recommendations)
        self.assertGreater(scores["Interestelar"], scores["Mad Max: Furia en el camino"])
        self.assertIn("Interestelar", [title["title"] for title in recommendations])
        self.assertTrue(
            all(float(title["score"]) > 0 for title in recommendations)
        )

    def test_primary_genre_preference_beats_a_secondary_genre_match(self) -> None:
        preferences = {genre: 3.0 for genre in GENRES}
        preferences["Crimen y misterio"] = 5.0

        recommendations = recommend_titles(preferences, minimum_score=2.5)

        self.assertTrue(recommendations)
        self.assertTrue(
            all(title["genres"][0] == "Crimen y misterio" for title in recommendations)
        )

    def test_strict_threshold_can_hide_valid_positive_candidates(self) -> None:
        preferences = {genre: 3.0 for genre in GENRES}
        preferences["Ciencia ficción"] = 5.0

        candidates = recommend_titles(preferences)
        perfect_matches = recommend_titles(preferences, minimum_score=5.0)

        self.assertTrue(candidates)
        self.assertEqual(perfect_matches, [])

    def test_disliking_a_title_primary_genre_can_remove_it(self) -> None:
        preferences = {genre: 3.0 for genre in GENRES}
        preferences["Comedia"] = 1.0
        preferences["Crimen y misterio"] = 5.0

        recommendations = recommend_titles(preferences)

        self.assertNotIn("Brooklyn Nine-Nine", [title["title"] for title in recommendations])

    def test_relu_turns_neutral_or_disliked_affinity_into_zero(self) -> None:
        preferences = {genre: 1.0 for genre in GENRES}
        raw_score, relu_score = score_title(CATALOG[0], preferences)

        self.assertLess(raw_score, 0)
        self.assertEqual(relu_score, 0)
        self.assertEqual(recommend_titles(preferences), [])

    def test_content_type_filter_only_returns_selected_format(self) -> None:
        preferences = {genre: 5.0 for genre in GENRES}

        recommendations = recommend_titles(preferences, "Serie")

        self.assertTrue(recommendations)
        self.assertTrue(all(title["kind"] == "Serie" for title in recommendations))

    def test_all_neutral_preferences_produce_no_positive_match(self) -> None:
        preferences = {genre: 3.0 for genre in GENRES}

        self.assertEqual(recommend_titles(preferences), [])


if __name__ == "__main__":
    unittest.main()

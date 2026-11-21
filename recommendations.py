from __future__ import annotations

from typing import TypedDict


GENRES = (
    "Ciencia ficción",
    "Fantasía",
    "Comedia",
    "Drama",
    "Acción y aventura",
    "Crimen y misterio",
    "Terror",
    "Romance",
    "Documental",
    "Animación",
)


class Title(TypedDict):
    title: str
    kind: str
    year: int
    genres: list[str]
    description: str


CATALOG: tuple[Title, ...] = (
    {
        "title": "Interestelar",
        "kind": "Película",
        "year": 2014,
        "genres": ["Ciencia ficción", "Drama", "Acción y aventura"],
        "description": "Un viaje espacial pone a prueba los vínculos familiares y la supervivencia humana.",
    },
    {
        "title": "La llegada",
        "kind": "Película",
        "year": 2016,
        "genres": ["Ciencia ficción", "Drama", "Crimen y misterio"],
        "description": "Una lingüista busca comunicarse con visitantes cuyo propósito es incierto.",
    },
    {
        "title": "Black Mirror",
        "kind": "Serie",
        "year": 2011,
        "genres": ["Ciencia ficción", "Drama", "Crimen y misterio"],
        "description": "Historias independientes exploran futuros inquietantes alrededor de la tecnología.",
    },
    {
        "title": "El señor de los anillos: La comunidad del anillo",
        "kind": "Película",
        "year": 2001,
        "genres": ["Fantasía", "Acción y aventura", "Drama"],
        "description": "Un grupo muy distinto emprende una misión decisiva en una tierra fantástica.",
    },
    {
        "title": "Harry Potter y la piedra filosofal",
        "kind": "Película",
        "year": 2001,
        "genres": ["Fantasía", "Acción y aventura"],
        "description": "Un joven descubre un mundo mágico y encuentra sus primeras amistades.",
    },
    {
        "title": "The Witcher",
        "kind": "Serie",
        "year": 2019,
        "genres": ["Fantasía", "Acción y aventura", "Drama"],
        "description": "Un cazador de monstruos recorre un continente lleno de magia y conflictos.",
    },
    {
        "title": "Paddington 2",
        "kind": "Película",
        "year": 2017,
        "genres": ["Comedia", "Acción y aventura"],
        "description": "Un oso entrañable intenta resolver un problema con ingenio y optimismo.",
    },
    {
        "title": "The Good Place",
        "kind": "Serie",
        "year": 2016,
        "genres": ["Comedia", "Fantasía"],
        "description": "Una mujer intenta convertirse en mejor persona en una vida después de la vida.",
    },
    {
        "title": "Brooklyn Nine-Nine",
        "kind": "Serie",
        "year": 2013,
        "genres": ["Comedia", "Crimen y misterio"],
        "description": "Un equipo policial resuelve casos mientras lidia con su peculiar vida laboral.",
    },
    {
        "title": "Sueños de fuga",
        "kind": "Película",
        "year": 1994,
        "genres": ["Drama", "Crimen y misterio"],
        "description": "Una amistad y una esperanza persistente crecen tras los muros de una prisión.",
    },
    {
        "title": "Gambito de dama",
        "kind": "Serie",
        "year": 2020,
        "genres": ["Drama", "Crimen y misterio"],
        "description": "Una prodigiosa ajedrecista busca su lugar mientras enfrenta desafíos personales.",
    },
    {
        "title": "This Is Us",
        "kind": "Serie",
        "year": 2016,
        "genres": ["Drama", "Romance"],
        "description": "Las historias de una familia se cruzan a través de distintas etapas de su vida.",
    },
    {
        "title": "Mad Max: Furia en el camino",
        "kind": "Película",
        "year": 2015,
        "genres": ["Acción y aventura", "Ciencia ficción"],
        "description": "Una huida por el desierto se convierte en una carrera por la libertad.",
    },
    {
        "title": "Misión imposible: Fallout",
        "kind": "Película",
        "year": 2018,
        "genres": ["Acción y aventura", "Crimen y misterio"],
        "description": "Un agente y su equipo intentan detener una amenaza contrarreloj.",
    },
    {
        "title": "One Piece",
        "kind": "Serie",
        "year": 2023,
        "genres": ["Acción y aventura", "Fantasía", "Comedia"],
        "description": "Una tripulación de amigos zarpa en busca de un tesoro legendario.",
    },
    {
        "title": "Entre navajas y secretos",
        "kind": "Película",
        "year": 2019,
        "genres": ["Crimen y misterio", "Comedia", "Drama"],
        "description": "Un detective reúne pistas y sospechosos tras una muerte inesperada.",
    },
    {
        "title": "Sherlock",
        "kind": "Serie",
        "year": 2010,
        "genres": ["Crimen y misterio", "Drama"],
        "description": "Un detective brillante resuelve casos en una Londres contemporánea.",
    },
    {
        "title": "Only Murders in the Building",
        "kind": "Serie",
        "year": 2021,
        "genres": ["Crimen y misterio", "Comedia"],
        "description": "Tres vecinos aficionados a los pódcast investigan un crimen en su edificio.",
    },
    {
        "title": "¡Huye!",
        "kind": "Película",
        "year": 2017,
        "genres": ["Terror", "Crimen y misterio", "Drama"],
        "description": "Una visita aparentemente cordial se transforma en una experiencia perturbadora.",
    },
    {
        "title": "Un lugar en silencio",
        "kind": "Película",
        "year": 2018,
        "genres": ["Terror", "Ciencia ficción", "Drama"],
        "description": "Una familia debe sobrevivir en un mundo donde hacer ruido es peligroso.",
    },
    {
        "title": "La maldición de Hill House",
        "kind": "Serie",
        "year": 2018,
        "genres": ["Terror", "Drama", "Crimen y misterio"],
        "description": "Una familia vuelve a enfrentarse a los secretos de una casa de su pasado.",
    },
    {
        "title": "Orgullo y prejuicio",
        "kind": "Película",
        "year": 2005,
        "genres": ["Romance", "Drama"],
        "description": "Dos personalidades obstinadas revisan sus primeras impresiones y sentimientos.",
    },
    {
        "title": "Cuestión de tiempo",
        "kind": "Película",
        "year": 2013,
        "genres": ["Romance", "Fantasía", "Comedia"],
        "description": "Un joven descubre una forma extraordinaria de cambiar pequeños momentos.",
    },
    {
        "title": "Normal People",
        "kind": "Serie",
        "year": 2020,
        "genres": ["Romance", "Drama"],
        "description": "Dos jóvenes construyen una relación que cambia con el paso de los años.",
    },
    {
        "title": "Free Solo",
        "kind": "Película",
        "year": 2018,
        "genres": ["Documental", "Acción y aventura"],
        "description": "Un escalador se prepara para afrontar una pared vertical sin cuerda.",
    },
    {
        "title": "Nuestro planeta",
        "kind": "Serie",
        "year": 2019,
        "genres": ["Documental", "Ciencia ficción"],
        "description": "Un recorrido por ecosistemas del planeta y los retos que enfrentan.",
    },
    {
        "title": "Mi maestro el pulpo",
        "kind": "Película",
        "year": 2020,
        "genres": ["Documental", "Drama"],
        "description": "Una amistad inesperada cambia la forma de observar la vida marina.",
    },
    {
        "title": "Coco",
        "kind": "Película",
        "year": 2017,
        "genres": ["Animación", "Fantasía", "Comedia"],
        "description": "Un niño músico descubre la historia de su familia en una tierra extraordinaria.",
    },
    {
        "title": "Spider-Man: Cruzando el multiverso",
        "kind": "Película",
        "year": 2023,
        "genres": ["Animación", "Acción y aventura", "Ciencia ficción"],
        "description": "Un joven héroe atraviesa mundos visualmente distintos y toma una difícil decisión.",
    },
    {
        "title": "Arcane",
        "kind": "Serie",
        "year": 2021,
        "genres": ["Animación", "Fantasía", "Drama"],
        "description": "Dos hermanas quedan en lados opuestos de un conflicto entre ciudades.",
    },
)

NEUTRAL_PREFERENCE = 3.0
AFFINITY_SCALE = 2.5
PRIMARY_GENRE_WEIGHT = 0.75
SECONDARY_GENRE_WEIGHT = 0.25


def relu(value: float) -> float:
    """Apply ReLU without changing positive values."""
    return max(0.0, value)


def score_title(title: Title, preferences: dict[str, float]) -> tuple[float, float]:
    """Return the raw heuristic score and its ReLU output in the range [0, 5]."""
    genres = title["genres"]
    primary_preference = preferences.get(genres[0], NEUTRAL_PREFERENCE)
    if len(genres) == 1:
        weighted_preference = primary_preference
    else:
        secondary_preferences = [
            preferences.get(genre, NEUTRAL_PREFERENCE) for genre in genres[1:]
        ]
        weighted_preference = (
            PRIMARY_GENRE_WEIGHT * primary_preference
            + SECONDARY_GENRE_WEIGHT
            * sum(secondary_preferences)
            / len(secondary_preferences)
        )

    raw_score = AFFINITY_SCALE * (weighted_preference - NEUTRAL_PREFERENCE)
    return raw_score, relu(raw_score)


def recommend_titles(
    preferences: dict[str, float],
    content_type: str = "Todo",
    minimum_score: float = 0.0,
) -> list[dict[str, object]]:
    """Return titles meeting the affinity threshold, ordered by score."""
    recommendations: list[dict[str, object]] = []
    for title in CATALOG:
        if content_type != "Todo" and title["kind"] != content_type:
            continue

        raw_score, score = score_title(title, preferences)
        if score > 0 and score >= minimum_score:
            recommendations.append(
                {
                    **title,
                    "raw_score": raw_score,
                    "score": score,
                }
            )

    return sorted(
        recommendations,
        key=lambda recommendation: (
            -float(recommendation["score"]),
            str(recommendation["title"]),
        ),
    )

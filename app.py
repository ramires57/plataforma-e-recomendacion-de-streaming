from __future__ import annotations

from html import escape

import pandas as pd
import streamlit as st

from recommendations import GENRES, recommend_titles, relu


ITEMS_BY_EXPERIENCE: dict[str, dict[str, float]] = {
    "Servicio de Streaming": {
        "Ciencia ficción": 8.0,
        "Comedia": 4.0,
        "Documentales": -3.0,
        "Drama": 6.0,
        "Terror": -7.0,
    },
    "Tienda en Línea": {
        "Auriculares": 9.0,
        "Libros": 5.0,
        "Cafetera": -4.0,
        "Mochila": 3.0,
        "Consola": -8.0,
    },
}

RATING_OPTIONS = {
    "No me gusta": 1.0,
    "Me interesa poco": 2.0,
    "Neutral": 3.0,
    "Me gusta": 4.0,
    "Me encanta": 5.0,
}

st.set_page_config(
    page_title="CineMatch | Recomendaciones",
    page_icon="🎬",
    layout="wide",
)

st.markdown(
    """
    <style>
    .stApp {
        background:
            radial-gradient(ellipse at 10% 0%, #301016 0, transparent 34%),
            #0d0e12;
        color: #f4f4f5;
    }
    .block-container { padding-top: 2rem; }
    .brand { color: #fb7185; font-size: .82rem; font-weight: 800;
             letter-spacing: .22em; text-transform: uppercase; }
    .movie-card {
        background: linear-gradient(145deg, #28242a, #17181d 72%);
        border: 1px solid #38363d; border-radius: 14px;
        min-height: 235px; padding: 18px; margin-bottom: 14px;
    }
    .movie-card .kind { color: #fda4af; font-size: .78rem;
                        font-weight: 700; text-transform: uppercase;
                        letter-spacing: .08em; }
    .movie-card h3 { color: #fff; font-size: 1.13rem; margin: .55rem 0; }
    .movie-card .meta { color: #b7b7c0; font-size: .86rem; }
    .movie-card .description { color: #e4e4e7; line-height: 1.45; }
    .movie-card .score { color: #86efac; font-weight: 700; }
    div[data-testid="stForm"] {
        background: #15161b; border: 1px solid #2e3038;
        border-radius: 14px; padding: 1rem 1.2rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="brand">CineMatch · Descubre tu próxima historia</div>', unsafe_allow_html=True)
st.title("¿Qué te gustaría ver hoy?")
st.caption(
    "Cuéntanos qué géneros disfrutas y armaremos una selección de películas y series."
)

page = st.radio(
    "Secciones",
    ["Para ti", "Demostración ReLU"],
    horizontal=True,
    label_visibility="collapsed",
)


def render_recommendations() -> None:
    profile_version = int(st.session_state.get("taste_profile_version", 0))
    header_columns = st.columns([4, 1])
    with header_columns[0]:
        st.subheader("Tus gustos")
    with header_columns[1]:
        if st.button("Empezar de nuevo"):
            st.session_state.pop("taste_preferences", None)
            st.session_state["taste_profile_version"] = profile_version + 1
            st.rerun()

    st.write("Responde estas 10 preguntas para conocer tus preferencias por género.")

    with st.form("taste_questionnaire"):
        columns = st.columns(2)
        preferences: dict[str, float] = {}
        for index, genre in enumerate(GENRES):
            with columns[index % 2]:
                answer = st.select_slider(
                    f"¿Cuánto te gusta **{genre.lower()}**?",
                    options=list(RATING_OPTIONS),
                    value="Neutral",
                    key=f"preference-{profile_version}-{genre}",
                )
                preferences[genre] = RATING_OPTIONS[answer]
        submitted = st.form_submit_button(
            "Ver mis recomendaciones",
            type="primary",
            width="stretch",
        )

    if submitted:
        st.session_state["taste_preferences"] = preferences

    saved_preferences = st.session_state.get("taste_preferences")
    if saved_preferences is None:
        st.info("Completa las 10 respuestas y pulsa «Ver mis recomendaciones».")
        return

    st.divider()
    st.subheader("Selección para ti")
    st.caption(
        "El género principal del título pesa más que los secundarios. "
        "Ajusta el umbral para ver solo coincidencias más fuertes."
    )
    filter_columns = st.columns([1, 1, 1.4])
    with filter_columns[0]:
        content_type = st.selectbox(
            "Formato",
            ["Todo", "Película", "Serie"],
        )
    with filter_columns[1]:
        result_limit = st.selectbox(
            "Mostrar",
            [6, 9, 12],
            index=1,
            format_func=lambda count: f"{count} títulos",
        )
    with filter_columns[2]:
        minimum_score = st.slider(
            "Afinidad mínima",
            min_value=0.0,
            max_value=5.0,
            value=1.5,
            step=0.5,
            format="%.1f / 5",
            help="Aumenta el umbral para mostrar solo coincidencias más fuertes.",
        )

    candidates = recommend_titles(saved_preferences, content_type)
    matches = [
        title for title in candidates if float(title["score"]) >= minimum_score
    ]
    fallback_matches = not matches and bool(candidates)

    if not candidates:
        st.info(
            "Tus respuestas no generan afinidad positiva todavía. "
            "Marca al menos un género como «Me gusta» o «Me encanta» y vuelve "
            "a pulsar «Ver mis recomendaciones»."
        )
        return

    if fallback_matches:
        shown_matches = candidates[: min(result_limit, 3)]
        st.info(
            f"Ningún título alcanza el umbral de {minimum_score:.1f}/5. "
            "Te mostramos las coincidencias positivas más cercanas; baja el "
            "umbral para ver más."
        )
    else:
        shown_matches = matches[:result_limit]

    st.caption(
        f"Ordenado por afinidad de género · {len(shown_matches)} de "
        f"{len(candidates)} coincidencias positivas"
    )

    result_columns = st.columns(3)
    for index, title in enumerate(shown_matches):
        genres = title["genres"]
        primary_genre = str(genres[0])
        preference_value = float(saved_preferences.get(primary_genre, 3.0))
        preference_label = next(
            (
                label
                for label, value in RATING_OPTIONS.items()
                if value == preference_value
            ),
            "Neutral",
        )
        secondary_genres = ", ".join(str(genre) for genre in genres[1:])
        genre_details = f"Principal: {escape(primary_genre)} · {escape(preference_label)}"
        if secondary_genres:
            genre_details += f"<br>También: {escape(secondary_genres)}"
        card = f"""
        <article class="movie-card">
          <div class="kind">{escape(str(title['kind']))} · {int(title['year'])}</div>
          <h3>{escape(str(title['title']))}</h3>
          <div class="meta">{genre_details}</div>
          <p class="description">{escape(str(title['description']))}</p>
          <div class="score">Afinidad ReLU: {float(title['score']):.1f} / 5</div>
        </article>
        """
        with result_columns[index % len(result_columns)]:
            st.markdown(card, unsafe_allow_html=True)

    st.caption(
        "La selección usa tus respuestas y las etiquetas de este catálogo de "
        "demostración. No consulta un servicio de streaming ni conoce tu historial."
    )


def render_relu_demo() -> None:
    st.subheader("Demostración de la activación")
    st.markdown(
        """
        Los valores editables **simulan las salidas previas de una red neuronal**.
        Esta sección demuestra la etapa de activación y agregación; **no entrena
        ni infiere una red**. El recomendador de la otra sección usa una regla
        transparente basada en tus respuestas, no una red neuronal.
        """
    )

    experience = st.selectbox(
        "Selecciona un contexto",
        options=list(ITEMS_BY_EXPERIENCE),
    )
    st.caption("Cada control permite elegir un valor entre -10 y +10.")

    defaults = ITEMS_BY_EXPERIENCE[experience]
    columns = st.columns(2)
    simulated_values: dict[str, float] = {}

    for index, (item, default) in enumerate(defaults.items()):
        with columns[index % len(columns)]:
            simulated_values[item] = st.slider(
                item,
                min_value=-10.0,
                max_value=10.0,
                value=default,
                step=0.5,
                format="%.1f",
                key=f"relu-{experience}-{item}",
            )

    results = [
        {
            "Ítem": item,
            "Salida simulada": value,
            "Salida ReLU": relu(value),
            "Estado": (
                "Positiva (conservada)"
                if value > 0
                else "Negativa (anulada)"
                if value < 0
                else "Cero"
            ),
        }
        for item, value in simulated_values.items()
    ]
    result_table = pd.DataFrame(results)

    st.subheader("Comparación por ítem")
    st.dataframe(
        result_table,
        hide_index=True,
        width="stretch",
        column_config={
            "Salida simulada": st.column_config.NumberColumn(format="%.1f"),
            "Salida ReLU": st.column_config.NumberColumn(format="%.1f"),
        },
    )

    st.subheader("Gráfico: antes y después de ReLU")
    chart_data = result_table.set_index("Ítem")[["Salida simulada", "Salida ReLU"]]
    st.bar_chart(chart_data, y_label="Valor de salida", height=350)

    original_sum = sum(simulated_values.values())
    relu_sum = sum(relu(value) for value in simulated_values.values())

    st.subheader("Agregación de demostración")
    st.caption(
        "Estas sumas ilustran el efecto de ReLU; no son una medida universal de "
        "afinidad ni una métrica de recomendación para sistemas reales."
    )
    metric_columns = st.columns(2)
    metric_columns[0].metric(
        "Suma original (sin ReLU), Σ xᵢ",
        f"{original_sum:.1f}",
    )
    metric_columns[1].metric(
        "Suma con ReLU, Σ max(0, xᵢ)",
        f"{relu_sum:.1f}",
        delta=f"{relu_sum - original_sum:.1f} frente a la suma original",
    )

    if relu_sum == 0:
        st.info("No hay ítems recomendados")
    else:
        recommended_items = [
            item for item, value in simulated_values.items() if relu(value) > 0
        ]
        st.success("Ítems con salida ReLU positiva: " + ", ".join(recommended_items))

    st.divider()
    st.caption(
        "Nota técnica: ReLU, f(x) = max(0, x), es una transformación elegida para "
        "esta demostración. En producción, descartar por completo las señales "
        "negativas no siempre es adecuado; la elección depende del modelo y del "
        "objetivo del recomendador."
    )


if page == "Para ti":
    render_recommendations()
else:
    render_relu_demo()

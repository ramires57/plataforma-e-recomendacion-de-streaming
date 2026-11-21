<<<<<<< HEAD
# CineMatch: recomendación por géneros y demostración de ReLU

Aplicación local y desplegable en Streamlit. Contesta 10 preguntas sobre tus
géneros favoritos para obtener películas y series ordenadas por afinidad desde
un catálogo de demostración. No necesita cuenta ni conexión a un servicio de
streaming.

## Ejecutar en Visual Studio Code

1. Abre esta carpeta en VS Code.
2. Crea y activa un entorno virtual desde la terminal integrada:

   **Windows (PowerShell):**

   ```powershell
   py -m venv .venv
   .\.venv\Scripts\Activate.ps1
   python -m pip install -r requirements.txt
   streamlit run app.py
   ```

   **macOS/Linux:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   python -m pip install -r requirements.txt
   streamlit run app.py
   ```

3. Abre la URL local que Streamlit muestra en la terminal (normalmente
   `http://localhost:8501`).

## Cómo se generan las recomendaciones

El cuestionario recoge una valoración de 1 a 5 para cada uno de 10 géneros.
El primer género etiquetado de cada título se considera principal y pesa 75%;
los secundarios comparten el 25% restante. Esto evita que un género principal
que no te interesa quede oculto por varios géneros neutrales. Después se centra
la afinidad ponderada en 3 (neutral), se multiplica por 2.5 y se aplica ReLU:

\[
s_{\mathrm{raw}}=2.5\cdot
\left(0.75p_{\mathrm{principal}}+
0.25\operatorname{media}(p_{\mathrm{secundarios}})-3\right),
\qquad
s_{\mathrm{ReLU}}=\max(0,s_{\mathrm{raw}}).
\]

Puedes filtrar por películas o series y ajustar el umbral mínimo de afinidad
(por defecto, 1.5/5); así se ocultan coincidencias débiles y se priorizan
títulos cuyo género principal sí valoraste. Cada tarjeta explica el género
principal y tu valoración. Si el umbral es demasiado alto, se muestran hasta
tres coincidencias positivas cercanas para que la pantalla no quede vacía.
Esta es una heurística transparente; **no es una red
neuronal entrenada ni una inferencia de un modelo**. El catálogo y sus etiquetas
son estáticos y orientativos.

La sección **Demostración ReLU** conserva controles editables entre -10 y +10
que simulan salidas previas de una red neuronal. ReLU conserva cada valor
positivo sin cambios y convierte valores negativos o iguales a cero en cero.
También compara las sumas originales y con ReLU. Si todas las salidas resultan
cero, se muestra **“No hay ítems recomendados”**. ReLU es una transformación de
demostración: descartar toda señal negativa no siempre es apropiado en un
recomendador real.

## Publicar en GitHub y Streamlit Community Cloud

1. Crea un repositorio vacío en GitHub y, desde esta carpeta, ejecuta:

   ```bash
   git init
   git add app.py recommendations.py test_recommendations.py requirements.txt README.md
   git commit -m "Add genre-based streaming recommendations"
   git branch -M main
   git remote add origin https://github.com/<usuario>/<repositorio>.git
   git push -u origin main
   ```

   Sustituye `<usuario>` y `<repositorio>` por los datos de tu repositorio.
2. En [Streamlit Community Cloud](https://share.streamlit.io/), inicia sesión
   con GitHub y selecciona **Create app**.
3. Elige el repositorio y la rama `main`, indica `app.py` como archivo principal
   y pulsa **Deploy**. Streamlit instalará las dependencias de
   `requirements.txt`.

## Pruebas

```bash
python -m unittest test_recommendations.py
```
=======
# plataforma-e-recomendacion-de-streaming
>>>>>>> 6bc44608412b73bde25b742731bb3dd14a81e0f7

import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc

# ================================
#   Cargar Dataset
# ================================
df = pd.read_csv("vehicles_us.csv")

# ================================
#   Inicializar App
# ================================
app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
server = app.server  # para despliegue en Render

# ================================
#   Layout
# ================================
app.layout = dbc.Container([
    dbc.Row([
        # ====== MENU LATERAL ======
        dbc.Col([
            html.H2("EDA Vehículos", className="text-center mt-3"),

            html.H5("Selecciona una gráfica:"),
            dcc.RadioItems(
                id="graph-selector",
                options=[
                    {"label": "Histograma: Odómetro", "value": "hist_odometer"},
                    {"label": "Histograma: Precio", "value": "hist_price"},
                    {"label": "Scatter: Precio vs Odómetro",
                        "value": "scatter_odometer_price"},
                    {"label": "Boxplot: Precio por Condición",
                        "value": "box_condition"},
                    {"label": "Scatter: Año vs Precio",
                        "value": "scatter_year_price"},
                ],
                value="hist_odometer",
                inputStyle={"margin-right": "6px", "margin-left": "15px"},
                style={"margin-top": "15px"}
            ),
        ],
            width=3, className="bg-light p-3 border-end"),

        # ====== CONTENIDO (GRÁFICAS) ======
        dbc.Col([
            html.H3("Visualización Interactiva", className="text-center mt-3"),
            dcc.Graph(id="main-graph", figure={})
        ], width=9),
    ])
], fluid=True)

# ================================
#   Callback para generar gráficas
# ================================


@app.callback(
    Output("main-graph", "figure"),
    Input("graph-selector", "value")
)
def update_graph(selected):

    if selected == "hist_odometer":
        fig = px.histogram(
            df, x="odometer", nbins=40,
            title="Distribución del Odómetro"
        )

    elif selected == "hist_price":
        fig = px.histogram(
            df, x="price", nbins=40,
            title="Distribución de los Precios"
        )

    elif selected == "scatter_odometer_price":
        fig = px.scatter(
            df, x="odometer", y="price", color="condition",
            title="Precio vs Odómetro"
        )

    elif selected == "box_condition":
        fig = px.box(
            df, x="condition", y="price",
            title="Distribución de Precios por Condición"
        )

    elif selected == "scatter_year_price":
        fig = px.scatter(
            df, x="model_year", y="price",
            title="Relación Año del Modelo vs Precio"
        )

    else:
        fig = {}

    fig.update_layout(template="plotly_white")
    return fig


# ================================
#   Ejecutar App
# ================================
if __name__ == "__main__":
    app.run_server(debug=True)

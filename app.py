import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

# ======================
# Cargar dataset
# ======================
df = pd.read_csv("vehicles_us.csv")

# ======================
# Inicializar app
# ======================
app = Dash(__name__)
server = app.server   # necesario para Render

# ======================
# Colores tema oscuro pastel
# ======================
colors = {
    "background": "#E0D6ED",  # fondo oscuro elegante
    "container": "#3D374F",   # tarjeta oscura
    "text": "#F8F8FF",
    "pastel_pink": "#E6BDCE",  # rosa pastel suave
    "pastel_lilac": "#D5C1F6",  # lila pastel
}

# ======================
# Layout con TABS
# ======================
app.layout = html.Div(
    style={"backgroundColor": colors["background"],
           "minHeight": "100vh", "padding": "20px"},
    children=[
        # Encabezado
        html.H1(
            "Dashboard de Vehículos - EDA Interactivo",
            style={
                "textAlign": "center",
                "padding": "15px",
                "backgroundColor": colors["pastel_lilac"],
                "borderRadius": "12px",
                "color": "#222",
                "fontWeight": "700",
                "marginBottom": "20px",
            },
        ),

        # Subheading
        html.H3(
            "Exploración de Datos en un Tema Oscuro con Tonos Pastel",
            style={
                "textAlign": "center",
                "padding": "10px",
                "backgroundColor": colors["pastel_pink"],
                "borderRadius": "10px",
                "color": "#333",
                "marginBottom": "30px",
            },
        ),

        # TABS
        dcc.Tabs(
            id="tabs-container",
            value="tab-hist",
            colors={
                "border": colors["pastel_lilac"],
                "primary": colors["pastel_pink"],
                "background": colors["container"],
            },
            children=[
                dcc.Tab(
                    label="Histogramas",
                    value="tab-hist",
                    style={
                        "backgroundColor": colors["container"], "color": colors["text"]},
                    selected_style={
                        "backgroundColor": colors["pastel_pink"], "color": "#222"},
                ),
                dcc.Tab(
                    label="Gráficas de Dispersión",
                    value="tab-scatter",
                    style={
                        "backgroundColor": colors["container"], "color": colors["text"]},
                    selected_style={
                        "backgroundColor": colors["pastel_lilac"], "color": "#222"},
                ),
                dcc.Tab(
                    label="Boxplots",
                    value="tab-box",
                    style={
                        "backgroundColor": colors["container"], "color": colors["text"]},
                    selected_style={
                        "backgroundColor": colors["pastel_pink"], "color": "#222"},
                ),
            ],
        ),

        html.Div(id="tab-content", style={"marginTop": "30px"}),
    ],
)

# ======================
# Contenido dinámico por TAB
# ======================


@app.callback(
    Output("tab-content", "children"),
    Input("tabs-container", "value")
)
def render_tab(tab):

    # TAB de Histogramas
    if tab == "tab-hist":
        return html.Div([
            dcc.Dropdown(
                id="hist-selector",
                options=[
                    {"label": "Odómetro", "value": "odometer"},
                    {"label": "Precio", "value": "price"},
                ],
                value="odometer",
                style={"width": "40%", "marginBottom": "20px"}
            ),
            dcc.Graph(id="hist-graph"),
        ])

    # TAB de Scatter
    elif tab == "tab-scatter":
        return html.Div([
            dcc.Dropdown(
                id="scatter-selector",
                options=[
                    {"label": "Precio vs Odómetro", "value": "odo_price"},
                    {"label": "Año vs Precio", "value": "yr_price"},
                ],
                value="odo_price",
                style={"width": "40%", "marginBottom": "20px"}
            ),
            dcc.Graph(id="scatter-graph"),
        ])

    # TAB de Boxplots
    elif tab == "tab-box":
        return html.Div([
            html.Label("Boxplot de precio por condición"),
            dcc.Graph(
                figure=px.box(
                    df, x="condition", y="price",
                    color="condition",
                    title="Distribución del precio según condición"
                ).update_layout(template="plotly_dark")
            )
        ])


# ======================
# Callbacks por gráfica
# ======================

# Histogramas
@app.callback(
    Output("hist-graph", "figure"),
    Input("hist-selector", "value")
)
def update_hist(col):
    fig = px.histogram(df, x=col, nbins=40,
                       title=f"Histograma de {col.capitalize()}")
    fig.update_layout(template="plotly_dark")
    return fig

# Scatter


@app.callback(
    Output("scatter-graph", "figure"),
    Input("scatter-selector", "value")
)
def update_scatter(option):

    if option == "odo_price":
        fig = px.scatter(df, x="odometer", y="price", color="condition",
                         title="Precio vs Odómetro")

    else:
        fig = px.scatter(df, x="model_year", y="price",
                         title="Año vs Precio")

    fig.update_layout(template="plotly_dark")
    return fig


# ======================
# Ejecutar
# ======================
if __name__ == "__main__":
    app.run_server(debug=True)

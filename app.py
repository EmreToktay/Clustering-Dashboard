# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 01:11:24 2023

@author: Memre
"""
from dash import Dash, html, Output, Input, State, dcc
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
import dash
from dash_iconify import DashIconify

def get_icon(icon):
    return DashIconify(icon=icon, height=16, color="#c2c7d0")


app = Dash(__name__,
           use_pages=True,
           external_stylesheets=[dbc.themes.BOOTSTRAP],
           meta_tags=[
               {"name": "viewport", "content": "width=device-width, initial-scale=1"}
             ],
            suppress_callback_exceptions=True
           )

server = app.server


app.layout = dmc.MantineProvider(
    theme={
        'fontFamily': '"Inter", sans-serif',
        "components": {
            "NavLink": {'styles': {'label': {'color': '#c2c7d0'}}}
        },
    },
    children=[
        dmc.Container([
            dmc.Navbar(
                p="md",
                fixed=False,
                width={"base": 400},
                hidden=True,
                hiddenBreakpoint='md',
                position='right',
                height='110vh',
                id='sidebar',
                children=[
                    html.Div(
                        [
                            dmc.NavLink(
                                opened=False,
                                label="Exploratory Data Analysis",
                                icon=get_icon(icon="tabler:gauge"),
                                rightSection=get_icon(icon="tabler-chevron-right"),
                                children=[
                                    dmc.NavLink(
                                        label="Option 1",
                                        href="/option1"  # Bu bir örnek. İstediğiniz URL'yi buraya ekleyebilirsiniz.
                                    ),
                                    dmc.NavLink(
                                        label="Option 2",
                                        href="/option2"  # Bu bir örnek. İstediğiniz URL'yi buraya ekleyebilirsiniz.
                                    )
                                ]
                            ),
                            dmc.NavLink(
                                opened=False,
                                label="Clustering",
                                icon=get_icon(icon="tabler:activity"),
                                rightSection=get_icon(icon="tabler-chevron-right"),
                                variant="subtle",
                                active=True,
                                children=[
                                    dmc.NavLink(
                                        label="DBscan",
                                        href="/dbscan"
                                    ),
                                    dmc.NavLink(
                                        label="Kmeans",
                                        href="/kmean"
                                    )
                                ]
                            ),
                        ],
                        style={'white-space': 'nowrap'},
                    )
                ], style={'overflow': 'hidden', 'transition': 'width 0.3s ease-in-out', 'background-color': '#343a40'}
            ),
            dmc.Container(
                id="page-container2",
                p=0,
                fluid=True,
                style={'backgroundColor': '#f4f6f9', 'width': '100%', 'margin': '0'},
                children=[
                    dmc.Header(
                        height=50,
                        p='10px',
                        style={"backgroundColor": ""},
                        children=[
                            dmc.Group(
                                position='apart',
                                children=[
                                    html.Div(
                                        dmc.Group(
                                            children=[
                                                dmc.MediaQuery([
                                                    dmc.Text([
                                                        dmc.Anchor("", href="",
                                                                   target="_blank",
                                                                   style={'textDecoration': 'none', 'color': '#457b9d'})
                                                    ], align='center', color="#a8dadc", weight=700)
                                                ], smallerThan='xs', styles={'fontSize': 12}),

                                                html.A(
                                                    dmc.Avatar(DashIconify(icon="mdi:github", width=25, color="#a8dadc"),  # '#24292f'
                                                               size="s", radius="s"),
                                                    href="https://github.com/EmreToktay/Clustering-Dashboard",
                                                    target="_blank",
                                                )
                                            ], spacing='xs', position='right'
                                        )
                                    )
                                ]
                            )
                        ]
                    ),
                    dash.page_container
                ],
            )
        ], size='100%', p=0, m=0, style={'display': 'flex'}
        )
    ]
)










dash.clientside_callback(
    """
    function handle_click_sidebar_width(n_clicks, width){
      const current_width = parseInt(width.base)
      console.log(current_width)
      if (n_clicks > 0 & current_width == 300) {
       return {base: 55};
      } else {
        return {base:300};
      }
    }
    """,
    Output("sidebar2", "width"),
    Input("sidebar-button2", "n_clicks"),
    State('sidebar2','width')
)


dash.clientside_callback(
    """

    function handle_heading_text(url){
      console.log(url)
      if (url === '/kmean') {
        return "KMean";
      } else if (url === '/dbscan') {
        return "DBScan";
      } else {
        return ""
     }
    }
    """,
    Output("ml-page", "children"),
    Input("url", "pathname")
)

if __name__ == '__main__':
	app.run_server(debug=True, port=8050)

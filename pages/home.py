# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 01:11:24 2023

@author: Memre
"""

import dash
from dash import html, dcc, Output, Input, State
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

dash.register_page(__name__, path='/')

intro_text = """
Welcome to my domain of data visualization using Python, powered by Plotly and Dash. This dashboard is designed to automate my customer clustering analysis. It's worth giving Dash a try.
Essentially, in the clustering segment, I follow a structured process, subsequently developing an app to automate [these steps](https://memretoktay.net/Blog%20Posts/plotly.html). Moreover,
this app provides the feature to export the clustered data back for further use.

About Dashboard i mainly focused on K-Means section due to best results for creditcard data set at Clustering Analyze. DBscan still need some improvements and didnt start for optics at all. They are now at my do list (good luck for them).

Please note that due to the resource constraints of the hosting platform, such as RAM and CPU limitations, there might be some initial lag in loading and processing times. However,
if preferred, you can follow the outlined steps below to run the dashboard locally on your machine.

Moreover, owing to the substantial size of the datasets, I could only upload 10% slices of each; the full dataset exceeds the platform's RAM capacity, making the processing impractical.
Here are the links to the[Original Datasets](https://www.kaggle.com/datasets/datascientistanna/customers-dataset). As an alternate data option,
 I've also included the complete data file `creditcard.csv`. If you're feeling adventurous, give a chance—sometimes it works smoothly. And if you wish to upload your own dataset for analysis,
 please bear this information in mind.
"""

instructions = """
1.  ** Use the git command:**
   \n```git clone https://github.com/EmreToktay/Clustering-Dashboard.git```\n
2.  ** Install necessary libraries using:**
   \n```pip install -r requirements.txt```\n
3.  ** With dependencies installed, run the application using:**
   \n```python app.py```\n
4.  ** After running `app.py`, open a web browser and navigate to:**
   \n```http://127.0.0.1:8050/```\n
6. **Note:**
   - Ensure you have both pip and git installed on your machine before starting.
   - For best practices, consider using a virtual environment (venv or conda) to install the dependencies,
     which can help avoid potential conflicts with other Python projects.
"""

layout = html.Div(
    children=[
        dmc.Paper(
            radius='lg',
            shadow='md',
            withBorder=True,
            m='md',
            p=20,
            children=[
                dmc.Text(
                    size=20,
                    align='center',
                    weight=700,
                    children="Clustering-Dashboard"
                ),
                dcc.Markdown(intro_text),
                dcc.Markdown(instructions)
            ],
            style={
                'width': '80%',
                'margin': '10px auto 0 auto',  # This line's margin value was updated.
                'backgroundColor': 'white',
                'textAlign': 'left',
            }
        )
    ],
    className='min-vh-100 d-flex flex-column justify-content-start align-items-center',  # This line's justify-content value was updated.
    style={"backgroundColor": "whitesmoke"}
)

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
Welcome to my data visualization domain with Python, thanks to Plotly and Dash. Due to the RAM and CPU limitations of the platform where I published, there might be initial delays in loading and processing times. If you wish, you can follow the steps listed below to run it locally.

Additionally, due to the large size of the datasets, I was able to upload only 10% slices of them; otherwise, the platform's RAM capacity is insufficient and processing becomes unfeasible. Links to the original datasets: [https://www.kaggle.com/datasets/datascientistanna/customers-dataset]. As a third option for the dataset, I included the full data file creditcard.csv. If you feel lucky, try to run it—sometimes it works :) Also, if you wish to upload your own data, please keep this information in mind.
"""

instructions = """
1. **Clone the Repository:**
   - Use the git command:
   \n```git clone https://github.com/EmreToktay/Clustering-Dashboard.git```\n
2. **Navigate to the Repository Folder:**
   - Once cloned, change to the directory using:
   \n```cd Clustering-Dashboard```\n
3. **Install Dependencies with the Requirements File:**
   - Install necessary libraries using:
   \n```pip install -r requirements.txt```\n
4. **Run the Application:**
   - With dependencies installed, run the application using:
   \n```python app.py```\n
5. **Access the Application Locally:**
   - After running `app.py`, open a web browser and navigate to:
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


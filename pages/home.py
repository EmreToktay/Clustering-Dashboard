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

layout = html.Div(
    children=[
        dmc.Paper(
            radius='lg',
            shadow='md',
            withBorder=True,
            m='md',
            p=20,
            children=[
                dmc.Stack(
                    children=[
                        dmc.Text(
                            size=40,
                            align='center',
                            weight=700,
                            children=[
                                'Machine Learning Dashboard!!!'    
                            ]    
                        )    
                    ]
                )
            ]   
        )
    ], className='min-vh-100 d-flex flex-column justify-content-center align-items-center', 
                 style={"backgroundColor": "silver"}
)
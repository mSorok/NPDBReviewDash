# -*- coding: utf-8 -*-
import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import pickle
import math
import dash_cytoscape as cyto
import dash_table
import plotly.graph_objs as go


##############
# texts

markdown_text_1 = '''
Explore the relationships and the diversity of Natural Products (NP) datasets.
Data available at [Zenodo](https://zenodo.org/record/3547718#.XeZCMZJKiu4) 
'''

markdown_text_2 = '''
Select the molecular descriptor in the dropdown menu. 
Only few databases are displayed by default, others can be selected by scrolling and clicking on the database menu on the right of the plot.
'''



##############
# functions

# get table data
df = pd.read_csv('NP_databases_review_open_only.csv')



# get network edges

def read_network_data(edges_file="percent_biway_sim2_10.csv", nodes_file="databases.csv"):
    nodes = set()
    cy_edges, cy_nodes = [], []

    elements = []

    fn = open(nodes_file, "r")
    for line in fn:
        if not line.startswith("NP_database,size,logsize"):
            dbname, dbsize, dblogsize = line.split(",")
            nodes.add(dbname)
            cy_nodes.append({"data": {"id": dbname, 'label': dbname, "size": dbsize }}) #'label': dbname,
            elements.append({"data": {"id": dbname, 'label': dbname, "size": math.log(int(dbsize))*10 }})

    fe = open(edges_file, "r")
    for line in fe:
        if not line.startswith("db1,db2,si"):
            source, target, score = line.split(",")

            if source in nodes and target in nodes:
                cy_edges.append({  # Add the Edge Node
                    'data': {'source': source, 'target': target, 'score': score, 'label': score}
                })
                elements.append({'data': {'source': source, 'target': target, 'score': score, 'label': score}})
    return elements


def create_cytoscape_stylesheet(min_score_display=60):
    style = []

    style.append(
        # Group selectors
        {
            'selector': 'node',
            'style': {
                'content': 'data(label)',
                'width': 'data(size)',
                'height': 'data(size)',
                "font-size": 18,
                "text-valign": "center",
                "text-halign": "center",
                'shape': 'ellipse',
                'background-color': 'floralWhite',
                'border-color': 'black',
                'border-width': '1px',


            }
        })
    style.append(
        {
            'selector': 'edge',
            'style': {
                'label': 'data(label)',
                'curve-style': 'segments',
                'target-arrow-shape': 'vee'
            }
        }
    )
    style.append(
        {
            'selector': '[score < ' + str(min_score_display) + ']',
            'style': {
                'display': 'none'
            }
        }
    )

    return style


# load hist scatterplots for npl_score:
def load_data(filename):
    infile = open(filename, "rb")
    dict_hist = pickle.load(infile)
    infile.close()
    return dict_hist


def create_hist_fig(file_with_path):
    dict_hists = load_data(file_with_path)
    figs = []

    for dbname in dict_hists.keys():
        if dbname not in ["supernatural2", "cmaup", "zinc_np"]:
            one_line = dict(
                x=dict_hists[dbname][1],
                y=dict_hists[dbname][0],
                text=dbname,
                name=dbname,
                mode='lines',
                visible= 'legendonly',
                line={'shape': 'spline', 'smoothing': 1.7}
                #opacity=0.7,
            )
            figs.append(one_line)
        else:
            one_line = dict(
                x=dict_hists[dbname][1],
                y=dict_hists[dbname][0],
                text=dbname,
                name=dbname,
                mode='lines',
                line={'shape': 'spline', 'smoothing': 1.7}
                # opacity=0.7,
            )
            figs.append(one_line)
    return figs




def create_dropdown_data():
    dropdown_data = [
        {'label': 'NP-likeness score', 'value': 'archive/npl_score_hist_backup'},
        #{'label': 'AlogP', 'value': 'archive/alogp_hist_backup'},
        {'label': 'Apolarity', 'value': 'archive/apol_hist_backup'},
        {'label': 'Eccentric Connectivity Index', 'value': 'archive/eccentricConnectivityIndexDescriptor_hist_backup'},
        {'label': 'FMF Descriptor', 'value': 'archive/fmfDescriptor_hist_backup'},
        {'label': 'Fragment Complexity Descriptor', 'value': 'archive/fragmentComplexityDescriptor_hist_backup'},
        {'label': 'fsp3', 'value': 'archive/fsp3_hist_backup'},
        {'label': 'Hybridization Ratio Descriptor', 'value': 'archive/hybridizationRatioDescriptor_hist_backup'},
        {'label': 'Kappa Shape Index', 'value': 'archive/kappaShapeIndex1_hist_backup'},
        {'label': 'Manhold logP', 'value': 'archive/manholdlogp_hist_backup'},
        {'label': 'Molecular Weight', 'value': 'archive/molecular_weight_hist_backup'},
        {'label': 'Petitjean Number', 'value': 'archive/petitjeanNumber_hist_backup'},
        {'label': 'Topological PSA', 'value': 'archive/topoPSA_hist_backup'},
        {'label': 'TPSA Efficiency', 'value': 'archive/tpsaEfficiency_hist_backup'},
        {'label': 'Vertex Adjacency Magnitude', 'value': 'archive/vertexAdjMagnitude_hist_backup'},
        {'label': 'Wiener Path Number', 'value': 'archive/weinerPathNumber_hist_backup'},
        {'label': 'Wiener Polarity Number', 'value': 'archive/weinerPolarityNumber_hist_backup'},
        {'label': 'XlogP', 'value': 'archive/xlogp_hist_backup'},
        {'label': 'Zagreb Index', 'value': 'archive/zagrebIndex_hist_backup'}
    ]
    return dropdown_data


dropdown_data_pretty = {
    'archive/npl_score_hist_backup': 'NP-likeness score',
    'archive/alogp_hist_backup': 'AlogP',
    'archive/apol_hist_backup': 'Apolarity',
    'archive/eccentricConnectivityIndexDescriptor_hist_backup': 'Eccentric Connectivity Index',
    'archive/fmfDescriptor_hist_backup': 'FMF Descriptor',
    'archive/fragmentComplexityDescriptor_hist_backup': 'Fragment Complexity Descriptor',
    'archive/fsp3_hist_backup': 'fsp3',
    'archive/hybridizationRatioDescriptor_hist_backup': 'Hybridization Ratio Descriptor',
    'archive/kappaShapeIndex1_hist_backup': 'Kappa Shape Index',
    'archive/manholdlogp_hist_backup': 'Manhold logP',
    'archive/molecular_weight_hist_backup': 'Molecular Weight',
    'archive/petitjeanNumber_hist_backup': 'Petitjean Number',
    'archive/topoPSA_hist_backup': 'Topological PSA',
    'archive/tpsaEfficiency_hist_backup': 'TPSA Efficiency',
    'archive/vertexAdjMagnitude_hist_backup': 'Vertex Adjacency Magnitude',
    'archive/weinerPathNumber_hist_backup': 'Wiener Path Number',
    'archive/weinerPolarityNumber_hist_backup': 'Wiener Polarity Number',
    'archive/xlogp_hist_backup': 'XlogP',
    'archive/zagrebIndex_hist_backup': 'Zagreb Index'
}


#############
# build the app

#external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__)

# Load extra layouts
# cyto.load_extra_layouts()

app.title = "Natural Product Databases Comparative Analysis"


app.layout = html.Div(children=[

    html.Div(className="pretty_container", children=[
        html.H1(children='Natural Product Databases: diversity in 2020'),

        dcc.Markdown(children=markdown_text_1),
    ]),

    # Histograms
    html.Div(className="pretty_container",children=[
        html.H4(children='Distributions of molecular descriptors for NPs in databases'),

        dcc.Markdown(children=markdown_text_2),

        #dcc.Input(id='my-id', value='archive/npl_score_hist_backup', type='text'),
        dcc.Dropdown(
            id='hist_dropdown',
            options=create_dropdown_data(),
            value='archive/npl_score_hist_backup'
        ),




        dcc.Graph(
            id='distributions-descriptors-graph',
        ),
    ]),

    html.Div(className="pretty_container", children=[
        html.H4(children='Overlap network between the NP datasets'),

        dcc.Slider(
            id='slider-for-cytoscape',
            min=10,
            max=100,
            marks={i: '{} %'.format(i) for i in range(10, 100, 5)},
            value=50,
        ),

        cyto.Cytoscape(
            id='cytoscape-all-db',
            layout={
                'name': 'random'
            },
            style={'width': '100%', 'height': '600px'},
            stylesheet=create_cytoscape_stylesheet(),
            elements=read_network_data()
        ),

    ]),

    html.Div(className="pretty_container",children=[

    html.H4(children='List of NP datasets and their caracteristics'),

        dash_table.DataTable(
            id='np-db-table',
            style_table={
                    'width': '100%',
                    'minWidth': '400px',
                    'overflowX': 'scroll',
                    'overflowY': 'scroll',
                    'height': '100%',
                },
            style_cell={
                    'minWidth': '80px', 'maxWidth': '200px', 'width': 'auto',
                    'whiteSpace': 'normal',
                    'height': 'auto',
                },
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict('records'),
            fixed_rows={'headers': True, 'data': 0},
            fixed_columns={ 'headers': True, 'data': 0},

        )
    ]),



])


@app.callback(
    Output('distributions-descriptors-graph', 'figure'),
    [Input('hist_dropdown', 'value')])
def update_distribution_histogram(selected_descriptor):
    return {'data': create_hist_fig(selected_descriptor),
            'layout': {
                'title': dropdown_data_pretty[selected_descriptor] + " distribution in NP databases",
                #(scroll the databases list and click on them to display the distribution)
                'xaxis': {
                    'title': dropdown_data_pretty[selected_descriptor],
                    'showgrid': False,
                },
                'yaxis': {
                    'title': "Density",
                    'showgrid': False,
                },
                'colorway': 'Rainbow'
            }}


@app.callback(
    Output('cytoscape-all-db','stylesheet'),
    [Input('slider-for-cytoscape', 'value')])
def update_cytoscape_visible_edges(selected_value):
    return create_cytoscape_stylesheet(selected_value)



if __name__ == '__main__':
    app.run_server(debug=True, host="0.0.0.0")

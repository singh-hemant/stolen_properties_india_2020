from dash import Dash, html, dcc, Input, Output
import pandas as pd
import plotly.express as px

# History color palette
colors = ['#012b3b','#2f1918', '#e2a946', '#e8d4a3', '#931c19', '#52221f']
# History of Scolar color palatte
colors1 = ['#c83d32', '#62a1a9', '#99af5d', '#e6b740', '#2b595a']


url = "stolen_properties.csv"
df = pd.read_csv(url, skiprows=[1, 8, 18])
#print(df.dtypes)


# --------------------------------------------- Dash App --------------------------------------------#
app = Dash(__name__)

app.layout = html.Div([
    html.Div([
        dcc.Markdown("""
            # Stolen Properties in india (2020)
            """)     
    ], style={'text-align':'center', 'padding':'20px'}),
    html.Br(),
    
    html.Div([
    dcc.Dropdown(
        df.columns[2:],
        'Number of Cases in which Property  Stolen',
        id="property_name")
    ], style={'width':'50%','float':'center','padding':'0px 20px 0px 20px'}),

    html.Br(),

    html.Div([
        dcc.Graph(id="plot1")
        ], style={'display':'block','float':'center','padding':'0px 20px 20px 20px'}),

    html.Br(),

    html.Div([
        dcc.Markdown("""
            ## Problem Statement
            
            >
                Finding out the different types of stolen properties in India in year 2020
            
            """)     
    ], style={'text-align':'left', 'padding':'20px', 'color':colors[0]}),

    html.Div([
        dcc.Markdown("""
            ## Data Description
            The dataset used in this is collected from Indian Govt. official website [data.gov.in](https://data.gov.in/)

            * This dataset has several columns which we can look into : -
            
                * **Sr. No.**

                * **Nature of Property** or the types of property getting stolen

                * **Number of cases registered of stolen properties**

                * **Percentage share of total stolen**

                * **Number of Cases in which Property Recovered**

                * **Percentage Detection of the stolen property**

                * **Total Value of stolen Property**

                * **Share to Total Stolen (in Valuation)**

                * **Value of Property - Recovered **

                * **Percentage Recovery**
            
            
            """, link_target="_blank")     
    ], style={'text-align':'left', 'padding':'20px', 'color':colors[1]}),

    html.Div([
        dcc.Markdown("""
            ## Our Findings
            ### Here are some findings we can get by plotting the graph.

                The most stolen thing is two wheelers(even more than mobile phones) which is kinda surprising
                being the size of the vehicle. One reason could be the unsecured parking lots.

                Most recovered items are the the big ones(i.e. buses, trucks, etc) and antiques. 

                

            

            
            
            """)     
    ], style={'text-align':'left', 'padding':'20px'}),
    
], style={'background-color':colors[3], 'font-family':'monospace', 'font-size':'20px', 'color':colors[4]})

@app.callback(
    Output('plot1', 'figure'),
    Input('property_name', 'value'))
def update_graph(value):
    dff = df.sort_values(value, ascending=False)
    fig = px.bar(dff, x='Nature of Property', y=value, color=value,
                 color_continuous_scale=px.colors.sequential.Hot_r)
    
    fig.update(layout_coloraxis_showscale=False)
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)

import pandas as pd
import requests
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------
# Fetch data from backend
# -----------------------------
try:
    prices = pd.DataFrame(requests.get("http://127.0.0.1:5000/api/prices").json())
    prices['Date'] = pd.to_datetime(prices['Date'])
    prices.sort_values('Date', inplace=True)
except Exception as e:
    print(f"Error fetching prices data: {e}")
    prices = pd.DataFrame(columns=['Date', 'Price'])

try:
    events = pd.DataFrame(requests.get("http://127.0.0.1:5000/api/events").json())
    events['Date'] = pd.to_datetime(events['Date'])
    events.sort_values('Date', inplace=True)
except Exception as e:
    print(f"Error fetching events data: {e}")
    events = pd.DataFrame(columns=['Date', 'Event'])

# -----------------------------
# Dash App
# -----------------------------
app = Dash(__name__)
app.title = "Brent Oil Market Analysis"

# -----------------------------
# Layout
# -----------------------------
app.layout = html.Div(style={'font-family': 'Helvetica, Arial, sans-serif', 'margin': '20px', 'backgroundColor': '#f9f9f9'}, children=[

    html.H1("Brent Oil Market Analysis Dashboard", style={'textAlign': 'center', 'color': '#2c3e50'}),
    html.H4("Historical Trends and Event Impacts", style={'textAlign': 'center', 'color': '#7f8c8d', 'margin-bottom': '40px'}),

    # KPI Cards
    html.Div(id='kpi-cards', style={'display': 'flex', 'justify-content': 'space-between', 'flex-wrap': 'wrap'}),

    # Date Range Picker
    html.Div(style={'margin-top': '40px', 'textAlign': 'center'}, children=[
        html.Label("Select Date Range:", style={'font-weight': 'bold', 'margin-right': '10px'}),
        dcc.DatePickerRange(
            id='date-range',
            start_date=prices['Date'].min() if not prices.empty else None,
            end_date=prices['Date'].max() if not prices.empty else None,
            display_format='YYYY-MM-DD'
        )
    ]),

    # Price Chart
    html.Div(style={'margin-top': '40px', 'padding': '20px', 'backgroundColor': 'white',
                    'border-radius': '8px', 'box-shadow': '0px 2px 10px rgba(0,0,0,0.1)'}, children=[
        dcc.Graph(id='price-chart')
    ]),

    # Event List
    html.Div(style={'margin-top': '40px', 'padding': '20px', 'backgroundColor': 'white',
                    'border-radius': '8px', 'box-shadow': '0px 2px 10px rgba(0,0,0,0.1)'}, children=[
        html.H4("Major Historical Events Impacting Oil Prices", style={'color': '#34495e'}),
        html.Ul(id='event-list')
    ])
])

# -----------------------------
# Callbacks
# -----------------------------
@app.callback(
    Output('kpi-cards', 'children'),
    Output('price-chart', 'figure'),
    Output('event-list', 'children'),
    Input('date-range', 'start_date'),
    Input('date-range', 'end_date')
)
def update_dashboard(start_date, end_date):
    filtered_prices = prices[(prices['Date'] >= start_date) & (prices['Date'] <= end_date)] if not prices.empty else pd.DataFrame(columns=['Date', 'Price'])
    filtered_events = events[(events['Date'] >= start_date) & (events['Date'] <= end_date)] if not events.empty else pd.DataFrame(columns=['Date', 'Event'])

    # KPIs
    avg_price = f"${filtered_prices['Price'].mean():,.2f}" if not filtered_prices.empty else "N/A"
    max_price = f"${filtered_prices['Price'].max():,.2f}" if not filtered_prices.empty else "N/A"
    min_price = f"${filtered_prices['Price'].min():,.2f}" if not filtered_prices.empty else "N/A"
    std_price = f"${filtered_prices['Price'].std():,.2f}" if not filtered_prices.empty else "N/A"

    kpi_cards = [
        html.Div(style={'backgroundColor': '#3498db', 'color': 'white', 'padding': '20px', 'border-radius': '8px',
                        'flex': '1', 'margin': '10px', 'textAlign': 'center', 'box-shadow': '0px 2px 8px rgba(0,0,0,0.1)'},
                 children=[html.H5("Average Price"), html.H2(avg_price)]),
        html.Div(style={'backgroundColor': '#2ecc71', 'color': 'white', 'padding': '20px', 'border-radius': '8px',
                        'flex': '1', 'margin': '10px', 'textAlign': 'center', 'box-shadow': '0px 2px 8px rgba(0,0,0,0.1)'},
                 children=[html.H5("Maximum Price"), html.H2(max_price)]),
        html.Div(style={'backgroundColor': '#e74c3c', 'color': 'white', 'padding': '20px', 'border-radius': '8px',
                        'flex': '1', 'margin': '10px', 'textAlign': 'center', 'box-shadow': '0px 2px 8px rgba(0,0,0,0.1)'},
                 children=[html.H5("Minimum Price"), html.H2(min_price)]),
        html.Div(style={'backgroundColor': '#f1c40f', 'color': 'white', 'padding': '20px', 'border-radius': '8px',
                        'flex': '1', 'margin': '10px', 'textAlign': 'center', 'box-shadow': '0px 2px 8px rgba(0,0,0,0.1)'},
                 children=[html.H5("Price Volatility"), html.H2(std_price)]),
    ]

    # Price Chart with Event Markers
    fig = go.Figure()
    if not filtered_prices.empty:
        fig.add_trace(go.Scatter(x=filtered_prices['Date'], y=filtered_prices['Price'],
                                 mode='lines+markers', name='Price',
                                 line=dict(color='#1f77b4'), marker=dict(size=4)))
    # Event markers
    if not filtered_events.empty:
        for _, row in filtered_events.iterrows():
            fig.add_trace(go.Scatter(
                x=[row['Date']], y=[filtered_prices[filtered_prices['Date']==row['Date']]['Price'].values[0] 
                                    if row['Date'] in filtered_prices['Date'].values else None],
                mode='markers+text',
                name=row['Event'],
                marker=dict(color='red', size=8, symbol='diamond'),
                text=[row['Event']],
                textposition='top center'
            ))

    fig.update_layout(title="Historical Brent Oil Prices with Events",
                      template='plotly_white',
                      xaxis_title='Date',
                      yaxis_title='Price (USD)',
                      title_x=0.5,
                      font=dict(family="Helvetica", size=12))

    # Event list as styled items
    event_list_items = [html.Li(f"{row['Date'].date()}: {row['Event']}", style={'margin-bottom': '5px'}) for _, row in filtered_events.iterrows()] \
                       if not filtered_events.empty else [html.P("No events in this range.")]

    return kpi_cards, fig, event_list_items


# -----------------------------
# Run App
# -----------------------------
if __name__ == '__main__':
    app.run(debug=True, port=8050)

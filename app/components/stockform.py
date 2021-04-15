from datetime import date, timedelta
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc

stock_form = dbc.Row(
    [
        dbc.Col(dbc.Input(placeholder="TICKR", id="tickr-input", className="mr-3"), align="center", width=3),

        dbc.Col(dcc.DatePickerRange(
            id='stock-date-picker-range',
            min_date_allowed=(date.today() - timedelta(days = 3*365)),
            max_date_allowed=date.today(),
            initial_visible_month=date.today()
        )),
        
        dbc.Col(dbc.Button("Filter", color="primary", id="form-submit"), width="3", align="center"),
    ],
    no_gutters=False,
    className="ml-auto flex-nowrap mt-md-0",
    align="end",
)

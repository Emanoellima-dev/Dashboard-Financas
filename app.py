from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dados import receita, despesas_num_positivo, imposto, Bancos, movimentacoes, tipo_movimentacao

app = Dash(external_stylesheets=[dbc.themes.QUARTZ])
server = app.server

fig1 = px.pie(tipo_movimentacao, names="Tipo", values="Quantidade de Movimentacoes", hole=0.5, title="Recebimentos VS Pagamentos", template="plotly_dark")
fig1.update_layout(
   plot_bgcolor="rgba(255, 255, 255, 0)",
   paper_bgcolor="rgba(255, 255, 255, 0.3)"
  )
fig1.update_traces(
   marker=dict(colors=["#f46acd","#1176f4"])
  )
  
fig2 = px.bar(Bancos, x="Banco", y="qtd de vendas", title="vendas por bancos", template="plotly_dark")
fig2.update_layout(
   plot_bgcolor="rgba(255, 255, 255, 0)",
   paper_bgcolor="rgba(255, 255, 255, 0.3)",
   yaxis=dict(
        showgrid=False,
    )
  )
fig2.update_traces(
   marker_color="#f46acd"
  )

fig3 = px.line(movimentacoes, x="data da movimentacao", y="qtd de movimentacoes", title="movimentações ao longo do ano", template="plotly_dark")
fig3.update_layout(
   plot_bgcolor="rgba(255, 255, 255, 0)",
   paper_bgcolor="rgba(255, 255, 255, 0.3)",
   yaxis=dict(
        showgrid=False
    ),
   xaxis=dict(
        showgrid=False
    ),
  )
fig3.update_traces(
   line=dict(color='#6b11a2')
  )

app.layout = dbc.Container([
  dbc.Row([
    dbc.Col([
       html.H1("Dashboard Financeiro", style={"text-align":"center", "margin-bottom":"1.5rem"})
      ])
    ]),
  
  dbc.Row([
    dbc.Col([
      dbc.Card([
        dbc.CardBody([
          html.H3("Receita"),
          html.H4(f"R$ {receita:,.2f}")
          ])
        ], style={"width":"16rem"})
      ]),
      
    dbc.Col([
      dbc.Card([
        dbc.CardBody([
          html.H3("Despesas"),
          html.H4(f"R$ {despesas_num_positivo:,.2f}")
          ])
        ], style={"width":"16rem"})
      ]),
      
    dbc.Col([
      dbc.Card([
        dbc.CardBody([
          html.H3("Imposto"),
          html.H4(f"R$ {imposto:,.2f}")
          ])
        ], style={"width":"16rem"})
      ]),
    ], style={"margin-bottom":"1.5rem"}),
    
  dbc.Row([
    dbc.Col([
      dcc.Graph(
        id="fig1",
        figure=fig1
        )
      ]),
      
    dbc.Col([
      dcc.Graph(
        id="fig2",
        figure=fig2
        )
      ])
    ], style={"margin-bottom":"1.5rem"}),
    
  dbc.Row([
    dbc.Col([
      dcc.Graph(
        id="fig3",
        figure=fig3
        )
      ])
    ])
  ], fluid=True)

if __name__ == "__main__":
  app.run(debug=True)
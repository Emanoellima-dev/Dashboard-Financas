import pandas as pd

df = pd.read_excel("Base Financeiro.xlsx", sheet_name="Planilha1", nrows=300)

# Receita
recebimento = df[df["Tipo"] == "Recebimento"]
receita = recebimento["Valor da Movimentação"].sum()

# Despesas
pagamento = df[df["Tipo"] == "Pagamento"]
despesas = pagamento["Valor da Movimentação"].sum()

numero_negativo = despesas
despesas_num_positivo = abs(numero_negativo)

# Imposto
imposto = receita * 0.15
num_imposto_formatado = f"{imposto:,.2f}"


Bancos = df["Banco"].value_counts().reset_index()
Bancos.columns = ["Banco", "qtd de vendas"]

movimentacoes = df["Data da Movimentacao"].value_counts().reset_index().sort_values(by="Data da Movimentacao")
movimentacoes.columns = ["data da movimentacao", "qtd de movimentacoes"]

tipo_movimentacao = df["Tipo"].value_counts().reset_index()
tipo_movimentacao.columns = ["Tipo", "Quantidade de Movimentacoes"]
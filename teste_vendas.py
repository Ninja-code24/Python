nome = str(input("digite o nome do vendedor: "))
a = float(input("digite o valor da venda de janeiro: $ "))
b = float(input("digite o valor da venda de fevereiro: $ "))
soma = (a+b)
media = (soma)/2
print("o vendedor {} obteve a media de suas vendas em R$ {:.2f} reais" .format(nome,media)) 
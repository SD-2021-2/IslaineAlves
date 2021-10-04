import xmlrpc.client

s = xmlrpc.client.ServerProxy("http://192.168.1.15:4000/")

#le o nome do cliente
print('Digite o nome do cliente: ')
nome = input()

#envia o nome ao servidor de aplicacao e mostra a resposta
resposta = s.calculaCredito(nome)
print(resposta)
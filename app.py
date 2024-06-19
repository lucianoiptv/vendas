from flask import Flask, request, render_template, jsonify
import os
from datetime import datetime

app = Flask(__name__)

# Define o diretório onde os arquivos de vendas serão armazenados
vendas_dir = os.path.join(os.getcwd(), 'vendas')
if not os.path.exists(vendas_dir):
    os.makedirs(vendas_dir)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/registrar-venda', methods=['POST'])
def registrar_venda():
    venda = request.json
    data = venda['data']
    conteudo = f"Vendedor: {venda['vendedor']}\n"
    conteudo += f"Local: {venda['local']}\n"
    conteudo += f"Valor: R$ {float(venda['valor']):.2f}\n"
    conteudo += f"Quantidade: {int(venda['quantidade'])}\n"
    conteudo += f"Forma de Pagamento: {venda['formaPagamento']}\n"
    if venda['formaPagamento'] == 'fiado':
        conteudo += f"Data p/ receber se Fiado: {venda['dataFiado']}\n"
    conteudo += f"Observação: {venda['observacao']}\n"
    conteudo += f"Total: R$ {float(venda['total']):.2f}\n\n"

    arquivo_vendas = os.path.join(vendas_dir, f'vendas_{data}.txt')
    with open(arquivo_vendas, 'a') as f:
       

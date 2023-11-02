import json
import os
from flask import Flask, render_template, url_for, request
from werkzeug.utils import secure_filename

import db_handler.analisa_csv_recebido as analisa_csv
import db_handler.conecta_banco_dados as conndb

UPLOAD_FOLDER = r'\static\_data\_data_in\\'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__, template_folder='templates_folder')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/info', methods=['GET'])
def info():
    return render_template('index.html')

@app.route('/data', methods=['POST', 'GET'])
def data():
    if request.method == 'POST':
        if 'file' not in request.files:
            return json.dumps({"Sem arquivo selecionado.":False}), 404 
        
        file = request.files['file']

        if file.filename == '':
            return json.dumps({"Sem arquivo selecionado.":False}), 404
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_path = os.path.dirname(os.path.realpath(__file__))+UPLOAD_FOLDER+filename
            file.save(os.path.join(upload_path))

            analisa_csv.analisa_csv_recebido(upload_path)
            analisa_csv.preenche_tabelas_auxiliares(upload_path)
            
            #send_file('./_data/_data_out/282.csv', attachment_filename='282.csv')
            return json.dumps({"Arquivo recebido." :True}), 200 
    
    if request.method == 'GET':
        return json.dumps({"GET method not implement" :False}), 404
    
    return json.dumps({"Problema nao identificado no recebimento do arquivo.":False}), 500

@app.route('/rodovia', methods=[ 'GET'])
def consulta_rodovia_info():
    data = request.json
    results = conndb.query_km_max_item(rodovia=data.get('rodovia'), item=data.get('item'))

    if results!=False:
        return json.dumps(results), 200
    else:
        return json.dumps({"Consulta nao foi possivel." :False}), 404

@app.route('/above_avg', methods=[ 'GET'])
def consulta_above_avg():
    data = request.json
    tabela = data.get('tabela')
    results = conndb.consulta_km_acima_media(tabela)

    if results!=False:
        return json.dumps(results), 200
    else:
        return json.dumps({"Consulta nao foi possivel." :False}), 404

if __name__ == "__main__":
    conndb.inicia_banco_dados()
    app.run()
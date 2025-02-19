from flask import Flask, jsonify, render_template
import os
import json
import threading
import requests
from dotenv import load_dotenv
import time
from payloads.lji import payloads as plji
from payloads.opq import payloads as popq
from payloads.mcp import payloads as pmcp
from flask_cors import CORS

load_dotenv()

url = os.getenv('url')
API_KEY = os.getenv('API_KEY')

headers = {
    "Content-Type": "application/json-rpc",
    "Authorization": f"Bearer {API_KEY}"
}

JSON_FOLDER_LJI = './jsons/lji'
JSON_FOLDER_OPQ = './jsons/opq'
JSON_FOLDER_MCP = './jsons/mcp'
PATH_INDEX = './templates'

def make_request(api_params, json_path):
    try:
        check = requests.get(url, headers=headers)

        if check.status_code == 200:
            response = requests.post(url, headers=headers, data=json.dumps(api_params))
            dados_json = response.json()

            with open(json_path, 'w') as json_file:
                json.dump(dados_json, json_file,indent=2)
        else:
            print('Não foi possivel estabelecer conexão')
    except Exception as e:
        print(f'ERRO ao realizar requisição, erro: {e}')

def request_loop(api_params,json_path):
    while True:
        make_request(api_params,json_path)
        time.sleep(30)

# faz os requests em loop
threads = [
    threading.Thread(target=request_loop, args=(plji.core_lji, './jsons/lji/core_lji.json')),
    threading.Thread(target=request_loop, args=(plji.ac1_lji, './jsons/lji/sw_ac1_lji.json')),
    threading.Thread(target=request_loop, args=(plji.ac2_lji, './jsons/lji/sw_ac2_lji.json')),
    threading.Thread(target=request_loop, args=(plji.ac3_lji, './jsons/lji/sw_ac3_lji.json')),
    threading.Thread(target=request_loop, args=(popq.core_opq, './jsons/opq/core_opq.json')),
    threading.Thread(target=request_loop, args=(popq.ac1_opq, './jsons/opq/sw_ac1_opq.json')),
    threading.Thread(target=request_loop, args=(popq.ac2_opq, './jsons/opq/sw_ac2_opq.json')),
    threading.Thread(target=request_loop, args=(popq.ac3_opq, './jsons/opq/sw_ac3_opq.json')),
    threading.Thread(target=request_loop, args=(pmcp.dist_mcp, './jsons/mcp/sw_dist_mcp.json')),
    threading.Thread(target=request_loop, args=(pmcp.iscsi, './jsons/mcp/sw_iscsi.json')),
    threading.Thread(target=request_loop, args=(pmcp.sw_core_mcp, './jsons/mcp/sw_core_mcp.json')),
    threading.Thread(target=request_loop, args=(pmcp.sw_audi_mcp, './jsons/mcp/sw_audi_mcp.json')),
    threading.Thread(target=request_loop, args=(pmcp.sw_multi_mcp, './jsons/mcp/sw_multi_mcp.json')),
    threading.Thread(target=request_loop, args=(pmcp.sw_nucad_mcp, './jsons/mcp/sw_nucad_mcp.json')),
    threading.Thread(target=request_loop, args=(pmcp.sw_ac_cpd_mcp, './jsons/mcp/sw_ac_cpd_mcp.json')),
    threading.Thread(target=request_loop, args=(pmcp.sw_semam_mcp, './jsons/mcp/sw_semam_mcp.json')),
    threading.Thread(target=request_loop, args=(pmcp.sw_ac_sepol_mcp, './jsons/mcp/sw_ac_sepol_mcp.json')),
    threading.Thread(target=request_loop, args=(pmcp.sw_ac_secos_mcp, './jsons/mcp/sw_ac_secos_mcp.json')),
    threading.Thread(target=request_loop, args=(pmcp.sw_ac_nutec_mcp, './jsons/mcp/sw_ac_nutec_mcp.json')),
    threading.Thread(target=request_loop, args=(pmcp.sw_ac_ol_rack1_mcp, './jsons/mcp/sw_ac_ol_rack1_mcp.json')),
    threading.Thread(target=request_loop, args=(pmcp.sw_ac_ol_rack2_mcp, './jsons/mcp/sw_ac_ol_rack2_mcp.json')),
    threading.Thread(target=request_loop, args=(pmcp.sw_ac_refeitorio_mcp, './jsons/mcp/sw_ac_refeitorio_mcp.json')),
    threading.Thread(target=request_loop, args=(pmcp.sw_ac_secad_rack1_mcp, './jsons/mcp/sw_ac_secad_rack1_mcp.json')),
    threading.Thread(target=request_loop, args=(pmcp.sw_ac_secad_rack2_mcp, './jsons/mcp/sw_ac_secad_rack2_mcp.json')),

]

for thread in threads:
    thread.daemon = True
    thread.start()

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/json/core_lji')
def serve_sw_core_lji():
    file_path = os.path.join(JSON_FOLDER_LJI, 'core_lji.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        
        response = jsonify(data)
        
        
        response.headers.add("Access-Control-Origin", "*")
        response.cache_control.no_cache = True  # Não usar cache
        response.cache_control.no_store = True  # Não armazenar
        response.cache_control.max_age = 0  # Sem tempo de cache
        return response
        
    else:
        return {"error": "File not found"}, 404

@app.route('/json/ac1_lji')
def serve_sw_ac1_lji():
    file_path = os.path.join(JSON_FOLDER_LJI, 'sw_ac1_lji.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        
        response = jsonify(data)
        
        
        response.headers.add("Access-Control-Origin", "*")
        response.cache_control.no_cache = True  # Não usar cache
        response.cache_control.no_store = True  # Não armazenar
        response.cache_control.max_age = 0  # Sem tempo de cache
        return response
        
    else:
        return {"error": "File not found"}, 404

@app.route('/json/ac2_lji')
def serve_sw_ac2_lji():
    file_path = os.path.join(JSON_FOLDER_LJI, 'sw_ac2_lji.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        
        response = jsonify(data)
        
        
        response.headers.add("Access-Control-Origin", "*")
        response.cache_control.no_cache = True  # Não usar cache
        response.cache_control.no_store = True  # Não armazenar
        response.cache_control.max_age = 0  # Sem tempo de cache
        return response
        
    else:
        return {"error": "File not found"}, 404

@app.route('/json/ac3_lji')
def serve_sw_ac3_lji():
    file_path = os.path.join(JSON_FOLDER_LJI, 'sw_ac3_lji.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        
        response = jsonify(data)
        
        
        response.headers.add("Access-Control-Origin", "*")
        response.cache_control.no_cache = True  # Não usar cache
        response.cache_control.no_store = True  # Não armazenar
        response.cache_control.max_age = 0  # Sem tempo de cache
        return response
        
    else:
        return {"error": "File not found"}, 404

@app.route('/json/core_opq')
def serve_sw_core_opq():
    file_path = os.path.join(JSON_FOLDER_OPQ, 'core_opq.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        
        response = jsonify(data)
        
        
        response.headers.add("Access-Control-Origin", "*")
        response.cache_control.no_cache = True  # Não usar cache
        response.cache_control.no_store = True  # Não armazenar
        response.cache_control.max_age = 0  # Sem tempo de cache
        return response
        
    else:
        return {"error": "File not found"}, 404

@app.route('/json/ac1_opq')
def serve_sw_ac1_opq():
    file_path = os.path.join(JSON_FOLDER_OPQ, 'sw_ac1_opq.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        
        response = jsonify(data)
        
        
        response.headers.add("Access-Control-Origin", "*")
        response.cache_control.no_cache = True  # Não usar cache
        response.cache_control.no_store = True  # Não armazenar
        response.cache_control.max_age = 0  # Sem tempo de cache
        return response
        
    else:
        return {"error": "File not found"}, 404

@app.route('/json/ac2_opq')
def serve_sw_ac2_opq():
    file_path = os.path.join(JSON_FOLDER_OPQ, 'sw_ac2_opq.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        
        response = jsonify(data)
        
        
        response.headers.add("Access-Control-Origin", "*")
        response.cache_control.no_cache = True  # Não usar cache
        response.cache_control.no_store = True  # Não armazenar
        response.cache_control.max_age = 0  # Sem tempo de cache
        return response
        
    else:
        return {"error": "File not found"}, 404

@app.route('/json/ac3_opq')
def serve_sw_ac3_opq():
    file_path = os.path.join(JSON_FOLDER_OPQ, 'sw_ac3_opq.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        
        response = jsonify(data)
        
        
        response.headers.add("Access-Control-Origin", "*")
        response.cache_control.no_cache = True  # Não usar cache
        response.cache_control.no_store = True  # Não armazenar
        response.cache_control.max_age = 0  # Sem tempo de cache
        return response
        
    else:
        return {"error": "File not found"}, 404

@app.route('/json/dist_mcp')
def serve_sw_dist_mcp():
    file_path = os.path.join(JSON_FOLDER_MCP, 'sw_dist_mcp.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        response = jsonify(data)

        response.headers.add("Access-Control-Origin", "*")
        response.cache_control.no_cache = True  # Não usar cache
        response.cache_control.no_store = True  # Não armazenar
        response.cache_control.max_age = 0  # Sem tempo de cache
        return response

    else:
        return {"error": "File not found"}, 404

@app.route('/json/iscsi')
def serve_sw_iscsi():
    file_path = os.path.join(JSON_FOLDER_MCP, 'sw_iscsi.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        response = jsonify(data)

        response.headers.add("Access-Control-Origin", "*")
        response.cache_control.no_cache = True  # Não usar cache
        response.cache_control.no_store = True  # Não armazenar
        response.cache_control.max_age = 0  # Sem tempo de cache
        return response

    else:
        return {"error": "File not found"}, 404

@app.route('/json/core_mcp')
def serve_sw_core_mcp():
    file_path = os.path.join(JSON_FOLDER_MCP, 'sw_core_mcp.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        response = jsonify(data)

        response.headers.add("Access-Control-Origin", "*")
        response.cache_control.no_cache = True  # Não usar cache
        response.cache_control.no_store = True  # Não armazenar
        response.cache_control.max_age = 0  # Sem tempo de cache
        return response

    else:
        return {"error": "File not found"}, 404

@app.route('/json/audi_mcp')
def serve_sw_audi_mcp():
    file_path = os.path.join(JSON_FOLDER_MCP, 'sw_audi_mcp.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        response = jsonify(data)

        response.headers.add("Access-Control-Origin", "*")
        response.cache_control.no_cache = True  # Não usar cache
        response.cache_control.no_store = True  # Não armazenar
        response.cache_control.max_age = 0  # Sem tempo de cache
        return response

    else:
        return {"error": "File not found"}, 404

@app.route('/json/multi_mcp')
def serve_sw_multi_mcp():
    file_path = os.path.join(JSON_FOLDER_MCP, 'sw_multi_mcp.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        response = jsonify(data)

        response.headers.add("Access-Control-Origin", "*")
        response.cache_control.no_cache = True  # Não usar cache
        response.cache_control.no_store = True  # Não armazenar
        response.cache_control.max_age = 0  # Sem tempo de cache
        return response

    else:
        return {"error": "File not found"}, 404

@app.route('/json/nucad_mcp')
def serve_sw_nucad_mcp():
    file_path = os.path.join(JSON_FOLDER_MCP, 'sw_nucad_mcp.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        response = jsonify(data)

        response.headers.add("Access-Control-Origin", "*")
        response.cache_control.no_cache = True  # Não usar cache
        response.cache_control.no_store = True  # Não armazenar
        response.cache_control.max_age = 0  # Sem tempo de cache
        return response

    else:
        return {"error": "File not found"}, 404

@app.route('/json/ac_cpd_mcp')
def serve_sw_ac_cpd_mcp():
    file_path = os.path.join(JSON_FOLDER_MCP, 'sw_ac_cpd_mcp.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        response = jsonify(data)

        response.headers.add("Access-Control-Origin", "*")
        response.cache_control.no_cache = True  # Não usar cache
        response.cache_control.no_store = True  # Não armazenar
        response.cache_control.max_age = 0  # Sem tempo de cache
        return response

    else:
        return {"error": "File not found"}, 404

@app.route('/json/semam_mcp')
def serve_sw_semam_mcp():
    file_path = os.path.join(JSON_FOLDER_MCP, 'sw_semam_mcp.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        response = jsonify(data)

        response.headers.add("Access-Control-Origin", "*")
        response.cache_control.no_cache = True  # Não usar cache
        response.cache_control.no_store = True  # Não armazenar
        response.cache_control.max_age = 0  # Sem tempo de cache
        return response

    else:
        return {"error": "File not found"}, 404

@app.route('/json/ac_sepol_mcp')
def serve_sw_ac_sepol_mcp():
    file_path = os.path.join(JSON_FOLDER_MCP, 'sw_ac_sepol_mcp.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        response = jsonify(data)

        response.headers.add("Access-Control-Origin", "*")
        response.cache_control.no_cache = True  # Não usar cache
        response.cache_control.no_store = True  # Não armazenar
        response.cache_control.max_age = 0  # Sem tempo de cache
        return response

    else:
        return {"error": "File not found"}, 404

@app.route('/json/ac_secos_mcp')
def serve_sw_ac_secos_mcp():
    file_path = os.path.join(JSON_FOLDER_MCP, 'sw_ac_secos_mcp.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        response = jsonify(data)

        response.headers.add("Access-Control-Origin", "*")
        response.cache_control.no_cache = True  # Não usar cache
        response.cache_control.no_store = True  # Não armazenar
        response.cache_control.max_age = 0  # Sem tempo de cache
        return response

    else:
        return {"error": "File not found"}, 404

@app.route('/json/ac_nutec_mcp')
def serve_sw_ac_nutec_mcp():
    file_path = os.path.join(JSON_FOLDER_MCP, 'sw_ac_nutec_mcp.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        response = jsonify(data)

        response.headers.add("Access-Control-Origin", "*")
        response.cache_control.no_cache = True  # Não usar cache
        response.cache_control.no_store = True  # Não armazenar
        response.cache_control.max_age = 0  # Sem tempo de cache
        return response

    else:
        return {"error": "File not found"}, 404

@app.route('/json/ac_ol_r1_mcp')
def serve_sw_ac_ol_r1_mcp():
    file_path = os.path.join(JSON_FOLDER_MCP, 'sw_ac_ol_rack1_mcp.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        response = jsonify(data)

        response.headers.add("Access-Control-Origin", "*")
        response.cache_control.no_cache = True  # Não usar cache
        response.cache_control.no_store = True  # Não armazenar
        response.cache_control.max_age = 0  # Sem tempo de cache
        return response

    else:
        return {"error": "File not found"}, 404

@app.route('/json/ac_ol_r2_mcp')
def serve_sw_ac_ol_r2_mcp():
    file_path = os.path.join(JSON_FOLDER_MCP, 'sw_ac_ol_rack2_mcp.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        response = jsonify(data)

        response.headers.add("Access-Control-Origin", "*")
        response.cache_control.no_cache = True  # Não usar cache
        response.cache_control.no_store = True  # Não armazenar
        response.cache_control.max_age = 0  # Sem tempo de cache
        return response

    else:
        return {"error": "File not found"}, 404

@app.route('/json/ac_refeitorio_mcp')
def serve_sw_ac_refeitorio_mcp():
    file_path = os.path.join(JSON_FOLDER_MCP, 'sw_ac_refeitorio_mcp.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        response = jsonify(data)

        response.headers.add("Access-Control-Origin", "*")
        response.cache_control.no_cache = True  # Não usar cache
        response.cache_control.no_store = True  # Não armazenar
        response.cache_control.max_age = 0  # Sem tempo de cache
        return response

    else:
        return {"error": "File not found"}, 404

@app.route('/json/ac_secad_r1_mcp')
def serve_sw_ac_secad_r1_mcp():
    file_path = os.path.join(JSON_FOLDER_MCP, 'sw_ac_secad_rack1_mcp.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        response = jsonify(data)

        response.headers.add("Access-Control-Origin", "*")
        response.cache_control.no_cache = True  # Não usar cache
        response.cache_control.no_store = True  # Não armazenar
        response.cache_control.max_age = 0  # Sem tempo de cache
        return response

    else:
        return {"error": "File not found"}, 404

@app.route('/json/ac_secad_r2_mcp')
def serve_sw_ac_secad_r2_mcp():
    file_path = os.path.join(JSON_FOLDER_MCP, 'sw_ac_secad_rack2_mcp.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        response = jsonify(data)

        response.headers.add("Access-Control-Origin", "*")
        response.cache_control.no_cache = True  # Não usar cache
        response.cache_control.no_store = True  # Não armazenar
        response.cache_control.max_age = 0  # Sem tempo de cache
        return response

    else:
        return {"error": "File not found"}, 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000,debug=True)
    




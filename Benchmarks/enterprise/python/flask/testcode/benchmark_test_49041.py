# SPDX-License-Identifier: Apache-2.0
from cryptography.fernet import Fernet
import os
from flask import request, jsonify


request_state: dict[str, str] = {}

def BenchmarkTest49041():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    store_cred = os.environ.get('APP_SECRET', '')
    Fernet(store_cred.encode()).encrypt(str(data).encode())
    return jsonify({"result": "success"})

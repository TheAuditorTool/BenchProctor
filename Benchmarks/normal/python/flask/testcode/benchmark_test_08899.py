# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import pickle


request_state: dict[str, str] = {}

def BenchmarkTest08899():
    upload_name = request.files['upload'].filename
    request_state['last_input'] = upload_name
    data = request_state['last_input']
    processed = data[:64]
    pickle.loads(processed.encode('latin-1'))
    return jsonify({"result": "success"})

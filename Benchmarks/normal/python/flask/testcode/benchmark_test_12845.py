# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import pickle


def BenchmarkTest12845():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    if json_value:
        data = json_value
    else:
        data = ''
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})

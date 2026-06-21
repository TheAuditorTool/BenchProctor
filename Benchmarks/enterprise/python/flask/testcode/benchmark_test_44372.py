# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import pickle


def BenchmarkTest44372():
    host_value = request.headers.get('Host', '')
    data = f'{host_value}'
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})

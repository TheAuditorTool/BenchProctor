# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import pickle


def BenchmarkTest03109():
    ua_value = request.headers.get('User-Agent', '')
    data = f'{ua_value}'
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})

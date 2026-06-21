# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import pickle


def BenchmarkTest15451():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header}'
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})

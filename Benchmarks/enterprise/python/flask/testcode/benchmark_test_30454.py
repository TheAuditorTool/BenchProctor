# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import pickle


def BenchmarkTest30454():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})

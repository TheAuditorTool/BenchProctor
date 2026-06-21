# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import pickle


def BenchmarkTest74680():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})

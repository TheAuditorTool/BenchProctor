# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import pickle


def BenchmarkTest14333():
    auth_header = request.headers.get('Authorization', '')
    pickle.loads(auth_header.encode('latin-1'))
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import pickle


def BenchmarkTest50288():
    host_value = request.headers.get('Host', '')
    data = ' '.join(str(host_value).split())
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})

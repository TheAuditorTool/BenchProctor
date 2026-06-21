# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request, jsonify
import pickle


def BenchmarkTest06121():
    raw_body = request.get_data(as_text=True)
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})

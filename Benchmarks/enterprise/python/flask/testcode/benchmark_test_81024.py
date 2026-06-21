# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import pickle


def BenchmarkTest81024():
    upload_name = request.files['upload'].filename
    parts = str(upload_name).split(',')
    data = ','.join(parts)
    pickle.loads(data.encode('latin-1'))
    return jsonify({"result": "success"})

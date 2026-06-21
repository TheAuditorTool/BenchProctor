# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest12337():
    upload_name = request.files['upload'].filename
    data = ' '.join(str(upload_name).split())
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})

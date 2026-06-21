# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest08035():
    upload_name = request.files['upload'].filename
    data = f'{upload_name}'
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})

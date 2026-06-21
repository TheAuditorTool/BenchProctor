# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest26329():
    upload_name = request.files['upload'].filename
    data = ' '.join(str(upload_name).split())
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})

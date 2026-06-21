# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest15369():
    upload_name = request.files['upload'].filename
    data = upload_name if upload_name else 'default'
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest42583():
    upload_name = request.files['upload'].filename
    if upload_name:
        data = upload_name
    else:
        data = ''
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})

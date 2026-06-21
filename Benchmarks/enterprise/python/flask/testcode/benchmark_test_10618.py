# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10618():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})

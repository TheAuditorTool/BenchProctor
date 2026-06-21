# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest04039():
    upload_name = request.files['upload'].filename
    def normalize(value):
        return value.strip()
    data = normalize(upload_name)
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(data)}

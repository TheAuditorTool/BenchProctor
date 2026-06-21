# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest81271():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

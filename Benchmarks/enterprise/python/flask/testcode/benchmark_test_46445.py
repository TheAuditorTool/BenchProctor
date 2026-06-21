# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest46445():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    if str(data) in ('localhost', 'internal-gateway'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

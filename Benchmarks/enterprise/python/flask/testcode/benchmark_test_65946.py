# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest65946():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    if str(data) in ('localhost', 'internal-gateway'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

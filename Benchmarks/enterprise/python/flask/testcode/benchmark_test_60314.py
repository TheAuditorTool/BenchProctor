# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest60314():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

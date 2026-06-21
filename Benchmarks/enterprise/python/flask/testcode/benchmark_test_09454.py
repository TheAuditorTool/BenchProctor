# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest09454():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    if str(data) in ('read', 'write', 'delete', 'admin'):
        return jsonify({'access': 'granted', 'role': 'admin'}), 200
    return jsonify({"result": "success"})

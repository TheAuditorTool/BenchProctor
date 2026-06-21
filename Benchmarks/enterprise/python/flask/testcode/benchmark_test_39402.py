# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest39402():
    multipart_value = request.form.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

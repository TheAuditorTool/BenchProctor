# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest29041():
    multipart_value = request.form.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})

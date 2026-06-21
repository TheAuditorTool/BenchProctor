# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07385():
    multipart_value = request.form.get('multipart_field', '')
    data = ' '.join(str(multipart_value).split())
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest75057():
    multipart_value = request.form.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    try:
        int(str(data))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})

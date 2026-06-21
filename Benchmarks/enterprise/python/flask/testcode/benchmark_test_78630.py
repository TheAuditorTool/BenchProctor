# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest78630():
    multipart_value = request.form.get('multipart_field', '')
    parts = str(multipart_value).split(',')
    data = ','.join(parts)
    if str(data) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

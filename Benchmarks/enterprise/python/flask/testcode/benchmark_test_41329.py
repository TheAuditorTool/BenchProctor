# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest41329():
    multipart_value = request.form.get('multipart_field', '')
    if str(multipart_value) == 'fluffy':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

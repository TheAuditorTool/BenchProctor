# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest68810():
    multipart_value = request.form.get('multipart_field', '')
    if multipart_value:
        data = multipart_value
    else:
        data = ''
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

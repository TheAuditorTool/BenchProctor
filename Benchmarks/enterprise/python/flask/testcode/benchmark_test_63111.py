# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest63111():
    multipart_value = request.form.get('multipart_field', '')
    if len(str(multipart_value)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

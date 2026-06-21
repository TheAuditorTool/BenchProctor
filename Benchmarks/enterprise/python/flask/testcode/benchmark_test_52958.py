# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest52958():
    multipart_value = request.form.get('multipart_field', '')
    data, _sep, _rest = str(multipart_value).partition('\x00')
    if len(str(data)) >= 4:
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

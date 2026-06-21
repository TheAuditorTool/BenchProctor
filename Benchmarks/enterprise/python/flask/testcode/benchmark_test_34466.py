# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest34466():
    multipart_value = request.form.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    if str(data) in ('admin', 'true', 'authenticated'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

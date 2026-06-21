# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest14536():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value}'
    exec(str(data))
    return jsonify({"result": "success"})

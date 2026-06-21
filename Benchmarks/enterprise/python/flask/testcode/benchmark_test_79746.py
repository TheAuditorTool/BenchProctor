# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79746():
    multipart_value = request.form.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    eval(str(data))
    return jsonify({"result": "success"})

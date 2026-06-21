# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest77552():
    multipart_value = request.form.get('multipart_field', '')
    int(str(multipart_value))
    return jsonify({"result": "success"})

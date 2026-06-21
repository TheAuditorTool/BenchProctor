# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest46623():
    multipart_value = request.form.get('multipart_field', '')
    exec(str(multipart_value))
    return jsonify({"result": "success"})

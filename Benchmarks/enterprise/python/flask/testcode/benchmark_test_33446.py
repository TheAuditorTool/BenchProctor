# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest33446():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    int(str(data))
    return jsonify({"result": "success"})

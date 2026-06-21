# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest69183():
    multipart_value = request.form.get('multipart_field', '')
    data = unquote(multipart_value)
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})

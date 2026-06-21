# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest79829():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    int(str(data))
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from flask import session
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest16251():
    field_value = request.form.get('field', '')
    data = unquote(field_value)
    session['data'] = str(data)
    return jsonify({"result": "success"})

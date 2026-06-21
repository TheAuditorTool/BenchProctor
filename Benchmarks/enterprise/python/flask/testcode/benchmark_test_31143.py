# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest31143():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    session['data'] = str(data)
    return jsonify({"result": "success"})

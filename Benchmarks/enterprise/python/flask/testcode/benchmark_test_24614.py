# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest24614():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    session['user'] = str(data)
    return jsonify({"result": "success"})

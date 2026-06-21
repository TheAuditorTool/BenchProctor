# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest16654():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    session['user'] = str(data)
    return jsonify({"result": "success"})

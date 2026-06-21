# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest61511():
    field_value = request.form.get('field', '')
    data = (lambda v: v.strip())(field_value)
    session['data'] = str(data)
    return jsonify({"result": "success"})

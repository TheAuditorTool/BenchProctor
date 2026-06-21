# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest24739():
    field_value = request.form.get('field', '')
    session['data'] = str(field_value)
    return jsonify({"result": "success"})

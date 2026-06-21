# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest14734():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    session['data'] = str(data)
    return jsonify({"result": "success"})

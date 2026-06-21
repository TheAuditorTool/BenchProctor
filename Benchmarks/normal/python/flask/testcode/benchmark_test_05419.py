# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest05419():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    session['user'] = str(data)
    return jsonify({"result": "success"})

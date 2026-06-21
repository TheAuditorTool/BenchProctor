# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest73302():
    field_value = request.form.get('field', '')
    data = '%s' % str(field_value)
    session['data'] = str(data)
    return jsonify({"result": "success"})

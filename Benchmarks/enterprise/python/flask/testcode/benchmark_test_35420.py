# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest35420():
    field_value = request.form.get('field', '')
    data = '%s' % (field_value,)
    session['user'] = str(data)
    return jsonify({"result": "success"})

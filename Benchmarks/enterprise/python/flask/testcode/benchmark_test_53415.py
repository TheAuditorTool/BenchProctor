# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify


def BenchmarkTest53415():
    field_value = request.form.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    session['data'] = str(processed)
    return jsonify({"result": "success"})

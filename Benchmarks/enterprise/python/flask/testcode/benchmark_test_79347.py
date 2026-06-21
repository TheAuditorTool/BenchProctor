# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest79347():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    eval(str(processed))
    return jsonify({"result": "success"})

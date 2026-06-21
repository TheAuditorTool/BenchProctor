# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest53695():
    field_value = request.form.get('field', '')
    prefix = ''
    data = prefix + str(field_value)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})

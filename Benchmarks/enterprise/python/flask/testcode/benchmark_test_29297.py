# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest29297():
    field_value = request.form.get('field', '')
    data = '%s' % (field_value,)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})

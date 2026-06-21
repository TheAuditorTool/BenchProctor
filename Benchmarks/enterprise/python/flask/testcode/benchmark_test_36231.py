# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest36231():
    field_value = request.form.get('field', '')
    parts = str(field_value).split(',')
    data = ','.join(parts)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})

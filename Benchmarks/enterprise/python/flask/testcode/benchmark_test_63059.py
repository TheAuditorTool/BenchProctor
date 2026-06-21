# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest63059():
    field_value = request.form.get('field', '')
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})

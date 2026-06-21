# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest18906():
    field_value = request.form.get('field', '')
    data = ' '.join(str(field_value).split())
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})

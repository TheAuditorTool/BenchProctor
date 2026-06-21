# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest26370():
    field_value = request.form.get('field', '')
    data = field_value if field_value else 'default'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})

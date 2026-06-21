# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35527():
    field_value = request.form.get('field', '')
    data, _sep, _rest = str(field_value).partition('\x00')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})

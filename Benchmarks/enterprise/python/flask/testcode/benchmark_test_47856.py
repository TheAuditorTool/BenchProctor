# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest47856():
    field_value = request.form.get('field', '')
    data = str(field_value).replace('\x00', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})

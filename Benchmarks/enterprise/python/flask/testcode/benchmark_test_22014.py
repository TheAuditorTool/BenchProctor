# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22014():
    field_value = request.form.get('field', '')
    data = f'{field_value:.200s}'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})

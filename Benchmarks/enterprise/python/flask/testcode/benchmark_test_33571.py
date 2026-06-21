# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest33571():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest10678():
    field_value = request.form.get('field', '')
    if field_value:
        data = field_value
    else:
        data = ''
    with open('/var/app/data/' + str(data), 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03351():
    field_value = request.form.get('field', '')
    data = '%s' % (field_value,)
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})

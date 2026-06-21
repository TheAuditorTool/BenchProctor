# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest55443():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value}'
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})

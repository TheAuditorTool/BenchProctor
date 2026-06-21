# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest17171():
    multipart_value = request.form.get('multipart_field', '')
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(str(multipart_value))
    return jsonify({"result": "success"})

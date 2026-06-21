# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61224():
    multipart_value = request.form.get('multipart_field', '')
    data = f'{multipart_value}'
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})

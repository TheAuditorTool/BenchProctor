# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest20240():
    multipart_value = request.form.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})

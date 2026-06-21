# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest64685():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})

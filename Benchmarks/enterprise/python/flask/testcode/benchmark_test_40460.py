# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest40460():
    multipart_value = request.form.get('multipart_field', '')
    prefix = ''
    data = prefix + str(multipart_value)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})

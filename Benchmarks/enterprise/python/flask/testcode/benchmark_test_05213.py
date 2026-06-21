# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest05213():
    raw_body = request.get_data(as_text=True)
    prefix = ''
    data = prefix + str(raw_body)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest52254():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % (header_value,)
    with open('/var/log/app_audit.log', 'a') as fh:
        fh.write(str(data))
    return jsonify({"result": "success"})

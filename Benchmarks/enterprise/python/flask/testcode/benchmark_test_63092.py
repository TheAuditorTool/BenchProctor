# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest63092():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '{}'.format(forwarded_ip)
    exec(str(data))
    return jsonify({"result": "success"})

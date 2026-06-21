# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest62054():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = str(forwarded_ip).replace('\x00', '')
    int(str(data))
    return jsonify({"result": "success"})

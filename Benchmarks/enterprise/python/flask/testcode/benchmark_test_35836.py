# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest35836():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = str(forwarded_ip).replace('\x00', '')
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})

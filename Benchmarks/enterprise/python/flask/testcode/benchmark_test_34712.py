# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest34712():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = f'{forwarded_ip:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})

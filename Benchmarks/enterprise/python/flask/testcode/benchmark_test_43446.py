# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest43446():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = f'{forwarded_ip:.200s}'
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return jsonify({"result": "success"})

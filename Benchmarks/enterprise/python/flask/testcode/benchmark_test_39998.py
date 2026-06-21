# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest39998():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = to_text(forwarded_ip)
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(data)
    if origin in allowed:
        return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': origin}
    return jsonify({"result": "success"})

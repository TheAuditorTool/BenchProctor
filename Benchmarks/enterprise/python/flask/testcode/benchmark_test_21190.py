# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest21190():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = relay_value(forwarded_ip)
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        return jsonify({'error': 'privilege drop failed'}), 500
    return jsonify({"result": "success"})

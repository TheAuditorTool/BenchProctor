# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json


def BenchmarkTest69615():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    try:
        data = json.loads(forwarded_ip).get('value', forwarded_ip)
    except (json.JSONDecodeError, AttributeError):
        data = forwarded_ip
    return jsonify({'status': 'ok'}), 200, {'X-Echo': str(data)}

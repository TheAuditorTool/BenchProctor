# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest81483():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    try:
        int(str(forwarded_ip))
    except ValueError:
        return jsonify({'error': 'invalid'}), 400
    return jsonify({"result": "success"})

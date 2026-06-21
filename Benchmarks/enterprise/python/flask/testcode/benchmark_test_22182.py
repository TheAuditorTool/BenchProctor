# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest22182():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    return jsonify({'status': 'ok'}), 200, {'Access-Control-Allow-Origin': str(forwarded_ip)}

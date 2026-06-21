# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest34539():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = '{}'.format(forwarded_ip)
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})

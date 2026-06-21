# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest47684():
    ua_value = request.headers.get('User-Agent', '')
    data = ua_value if ua_value else 'default'
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with open('output.csv', 'a') as fh:
        fh.write(str(processed) + ',data\n')
    return jsonify({"result": "success"})

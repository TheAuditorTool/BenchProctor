# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest11800():
    host_value = request.headers.get('Host', '')
    prefix = ''
    data = prefix + str(host_value)
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    eval(str(processed))
    return jsonify({"result": "success"})

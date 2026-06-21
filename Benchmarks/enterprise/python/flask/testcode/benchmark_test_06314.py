# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest06314():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % str(ua_value)
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})

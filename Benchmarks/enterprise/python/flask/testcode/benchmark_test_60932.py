# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest60932():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % (ua_value,)
    try:
        result = int(str(data))
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    return jsonify({"result": "success"})

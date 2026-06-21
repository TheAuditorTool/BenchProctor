# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest24156():
    ua_value = request.headers.get('User-Agent', '')
    parts = str(ua_value).split(',')
    data = ','.join(parts)
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})

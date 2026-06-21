# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest45737():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = f'{forwarded_ip:.200s}'
    if not str(data).isdigit():
        raise ValueError('invalid input: ' + str(data))
    return jsonify({"result": "success"})

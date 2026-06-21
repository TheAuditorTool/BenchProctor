# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest51300():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = f'{forwarded_ip:.200s}'
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})

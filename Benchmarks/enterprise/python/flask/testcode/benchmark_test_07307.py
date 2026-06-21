# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest07307():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = f'{forwarded_ip}'
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})

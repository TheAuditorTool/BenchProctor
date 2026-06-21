# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest61892():
    origin_value = request.headers.get('Origin', '')
    prefix = ''
    data = prefix + str(origin_value)
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    eval(str(processed))
    return jsonify({"result": "success"})

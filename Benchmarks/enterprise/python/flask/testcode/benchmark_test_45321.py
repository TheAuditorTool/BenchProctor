# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest45321():
    host_value = request.headers.get('Host', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    eval(str(processed))
    return jsonify({"result": "success"})

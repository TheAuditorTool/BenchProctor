# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest71337():
    ua_value = request.headers.get('User-Agent', '')
    data = ' '.join(str(ua_value).split())
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})

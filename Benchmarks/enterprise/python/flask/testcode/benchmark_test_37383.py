# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37383():
    ua_value = request.headers.get('User-Agent', '')
    data = str(ua_value).replace('\x00', '')
    int(str(data))
    return jsonify({"result": "success"})

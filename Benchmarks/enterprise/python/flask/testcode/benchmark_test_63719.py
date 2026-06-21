# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest63719():
    ua_value = request.headers.get('User-Agent', '')
    data = '{}'.format(ua_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})

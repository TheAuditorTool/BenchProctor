# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest31310():
    referer_value = request.headers.get('Referer', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})

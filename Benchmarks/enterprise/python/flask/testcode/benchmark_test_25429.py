# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest25429():
    referer_value = request.headers.get('Referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})

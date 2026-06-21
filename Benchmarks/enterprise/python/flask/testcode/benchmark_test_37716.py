# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest37716():
    referer_value = request.headers.get('Referer', '')
    data = ' '.join(str(referer_value).split())
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})

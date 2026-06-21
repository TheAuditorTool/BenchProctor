# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest59904():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value:.200s}'
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})

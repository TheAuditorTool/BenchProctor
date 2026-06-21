# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest14347():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value:.200s}'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})

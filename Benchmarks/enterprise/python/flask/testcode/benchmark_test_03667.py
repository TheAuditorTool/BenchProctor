# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest03667():
    referer_value = request.headers.get('Referer', '')
    data = referer_value if referer_value else 'default'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})

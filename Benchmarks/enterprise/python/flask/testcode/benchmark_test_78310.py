# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest78310():
    referer_value = request.headers.get('Referer', '')
    data = str(referer_value).replace('\x00', '')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})

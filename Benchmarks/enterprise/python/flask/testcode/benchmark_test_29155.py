# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest29155():
    origin_value = request.headers.get('Origin', '')
    data = str(origin_value).replace('\x00', '')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})

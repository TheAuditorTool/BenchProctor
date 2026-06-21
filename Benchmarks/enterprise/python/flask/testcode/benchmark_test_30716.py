# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest30716():
    raw_body = request.get_data(as_text=True)
    data = str(raw_body).replace('\x00', '')
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return jsonify({"result": "success"})

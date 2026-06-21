# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest65467():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value:.200s}'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify


def BenchmarkTest12836():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value}'
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})

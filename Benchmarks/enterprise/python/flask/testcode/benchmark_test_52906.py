# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest52906():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = f'{json_value}'
    os.remove(str(data))
    return jsonify({"result": "success"})

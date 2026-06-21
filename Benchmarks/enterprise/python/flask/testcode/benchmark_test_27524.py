# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest27524():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    os.setuid(int(str(json_value)) if str(json_value).isdigit() else 0)
    return jsonify({"result": "success"})

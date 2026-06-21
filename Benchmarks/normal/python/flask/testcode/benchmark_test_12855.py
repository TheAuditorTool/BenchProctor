# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest12855():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    try:
        os.setuid(int(str(json_value)) if str(json_value).isdigit() else 65534)
    except OSError:
        pass
    return jsonify({"result": "success"})

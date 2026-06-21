# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest11542():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    base_name = os.path.basename(str(json_value))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return jsonify({"result": "success"})

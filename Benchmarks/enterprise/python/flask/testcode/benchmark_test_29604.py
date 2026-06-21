# SPDX-License-Identifier: Apache-2.0
import os
import json
from flask import request, jsonify


def BenchmarkTest29604():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = json.loads(json_value).get('value', '')
    os.remove(str(data))
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import json


def BenchmarkTest26242():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    try:
        data = json.loads(json_value).get('value', json_value)
    except (json.JSONDecodeError, AttributeError):
        data = json_value
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import json


def BenchmarkTest44981():
    user_id = request.args.get('id', '')
    try:
        data = json.loads(user_id).get('value', user_id)
    except (json.JSONDecodeError, AttributeError):
        data = user_id
    eval(str(data))
    return jsonify({"result": "success"})

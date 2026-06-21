# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest08306():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data, _sep, _rest = str(json_value).partition('\x00')
    auth_check('user', data)
    return jsonify({"result": "success"})

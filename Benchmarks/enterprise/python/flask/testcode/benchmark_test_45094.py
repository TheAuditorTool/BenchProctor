# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest45094():
    user_id = request.args.get('id', '')
    data = FormData(payload=user_id).payload
    if auth_check('user', str(data)):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})

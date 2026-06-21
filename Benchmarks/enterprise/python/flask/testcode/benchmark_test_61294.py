# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest61294():
    user_id = request.args.get('id', '')
    data = FormData(payload=user_id).payload
    auth_check('user', data)
    return jsonify({"result": "success"})

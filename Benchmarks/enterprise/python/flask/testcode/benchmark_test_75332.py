# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest75332():
    user_id = request.args.get('id', '')
    data = FormData(payload=user_id).payload
    result = 100 / int(str(data))
    return jsonify({"result": "success"})

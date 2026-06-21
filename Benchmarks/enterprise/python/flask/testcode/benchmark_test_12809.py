# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest12809():
    user_id = request.args.get('id', '')
    data = FormData(payload=user_id).payload
    try:
        result = int(str(data))
    except Exception:
        pass
    return jsonify({"result": "success"})

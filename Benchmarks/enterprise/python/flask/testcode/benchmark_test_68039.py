# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest68039():
    user_id = request.args.get('id', '')
    data = FormData(payload=user_id).payload
    exec(str(data))
    return jsonify({"result": "success"})

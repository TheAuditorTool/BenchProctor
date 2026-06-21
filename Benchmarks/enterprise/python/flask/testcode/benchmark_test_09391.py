# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest09391():
    user_id = request.args.get('id', '')
    data = FormData(payload=user_id).payload
    os.remove(str(data))
    return jsonify({"result": "success"})

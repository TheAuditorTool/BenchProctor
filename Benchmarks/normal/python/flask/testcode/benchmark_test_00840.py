# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest00840():
    user_id = request.args.get('id', '')
    data = FormData(payload=user_id).payload
    os.seteuid(65534)
    return jsonify({"result": "success"})

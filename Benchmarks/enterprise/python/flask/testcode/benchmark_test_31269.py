# SPDX-License-Identifier: Apache-2.0
import threading
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest31269():
    user_id = request.args.get('id', '')
    data = FormData(payload=user_id).payload
    globals()['counter'] = int(data)
    return jsonify({"result": "success"})

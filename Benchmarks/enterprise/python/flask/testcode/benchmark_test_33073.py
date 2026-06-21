# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import importlib


@dataclass
class FormData:
    payload: str

def BenchmarkTest33073():
    user_id = request.args.get('id', '')
    data = FormData(payload=user_id).payload
    importlib.import_module(str(data))
    return jsonify({"result": "success"})

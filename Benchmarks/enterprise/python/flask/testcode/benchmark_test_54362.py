# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import os
from flask import jsonify
import importlib


@dataclass
class FormData:
    payload: str

def BenchmarkTest54362():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    importlib.import_module(str(data))
    return jsonify({"result": "success"})

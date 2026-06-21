# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
import os
from flask import jsonify
import importlib
import sys


@dataclass
class FormData:
    payload: str

def BenchmarkTest09841():
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})

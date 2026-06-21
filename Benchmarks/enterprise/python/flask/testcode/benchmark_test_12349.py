# SPDX-License-Identifier: Apache-2.0
from dataclasses import dataclass
from flask import request, jsonify
import importlib
import sys


@dataclass
class FormData:
    payload: str

def BenchmarkTest12349():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    sys.path.insert(0, str(data))
    importlib.import_module('report_renderer')
    return jsonify({"result": "success"})

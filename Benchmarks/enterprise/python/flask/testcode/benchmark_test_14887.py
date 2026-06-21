# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest14887():
    origin_value = request.headers.get('Origin', '')
    data = FormData(payload=origin_value).payload
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})

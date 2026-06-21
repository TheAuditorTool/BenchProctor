# SPDX-License-Identifier: Apache-2.0
import subprocess
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest57362():
    origin_value = request.headers.get('Origin', '')
    data = FormData(payload=origin_value).payload
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
import subprocess
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest37957():
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})

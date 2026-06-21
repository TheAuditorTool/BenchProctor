# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import request, jsonify
import subprocess


@dataclass
class FormData:
    payload: str

def BenchmarkTest72744():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})

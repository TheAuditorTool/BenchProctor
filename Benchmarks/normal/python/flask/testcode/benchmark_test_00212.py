# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import request, jsonify
import subprocess


@dataclass
class FormData:
    payload: str

def BenchmarkTest00212():
    auth_header = request.headers.get('Authorization', '')
    data = FormData(payload=auth_header).payload
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import request, jsonify
import subprocess


@dataclass
class FormData:
    payload: str

def BenchmarkTest58223():
    header_value = request.headers.get('X-Custom-Header', '')
    data = FormData(payload=header_value).payload
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})

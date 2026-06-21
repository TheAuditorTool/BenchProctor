# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest05958():
    ua_value = request.headers.get('User-Agent', '')
    data = FormData(payload=ua_value).payload
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})

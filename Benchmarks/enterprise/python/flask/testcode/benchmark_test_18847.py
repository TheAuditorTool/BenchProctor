# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest18847():
    user_id = request.args.get('id', '')
    data = FormData(payload=user_id).payload
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})

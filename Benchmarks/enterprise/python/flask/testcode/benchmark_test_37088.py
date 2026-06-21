# SPDX-License-Identifier: Apache-2.0
import subprocess
from dataclasses import dataclass
from flask import request, jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest37088():
    user_id = request.args.get('id', '')
    data = FormData(payload=user_id).payload
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})

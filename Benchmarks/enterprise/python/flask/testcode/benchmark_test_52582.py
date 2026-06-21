# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import request, jsonify
import subprocess


@dataclass
class FormData:
    payload: str

def BenchmarkTest52582():
    multipart_value = request.form.get('multipart_field', '')
    data = FormData(payload=multipart_value).payload
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})

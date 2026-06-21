# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import request, jsonify
import subprocess


@dataclass
class FormData:
    payload: str

def BenchmarkTest66266():
    raw_body = request.get_data(as_text=True)
    data = FormData(payload=raw_body).payload
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})

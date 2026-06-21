# SPDX-License-Identifier: Apache-2.0
import os
import re
from dataclasses import dataclass
from flask import request, jsonify
import subprocess


@dataclass
class FormData:
    payload: str

def BenchmarkTest04864():
    upload_name = request.files['upload'].filename
    data = FormData(payload=upload_name).payload
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    subprocess.run([str(processed), '--status'], shell=False)
    return jsonify({"result": "success"})

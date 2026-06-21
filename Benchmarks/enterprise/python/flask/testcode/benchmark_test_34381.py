# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
import base64
from flask import request, jsonify


def BenchmarkTest34381():
    raw_body = request.get_data(as_text=True)
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})

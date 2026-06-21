# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest36980():
    raw_body = request.get_data(as_text=True)
    data = str(raw_body).replace('\x00', '')
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})

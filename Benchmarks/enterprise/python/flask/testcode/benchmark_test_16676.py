# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest16676():
    raw_body = request.get_data(as_text=True)
    data = to_text(raw_body)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})

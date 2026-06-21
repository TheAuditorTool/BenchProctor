# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest62426():
    origin_value = request.headers.get('Origin', '')
    data = to_text(origin_value)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})

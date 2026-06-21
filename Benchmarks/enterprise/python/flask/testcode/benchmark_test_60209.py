# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def BenchmarkTest60209():
    raw_body = request.get_data(as_text=True)
    data = f'{raw_body}'
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def BenchmarkTest70458():
    origin_value = request.headers.get('Origin', '')
    data = f'{origin_value:.200s}'
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})

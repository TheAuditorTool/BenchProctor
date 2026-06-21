# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def BenchmarkTest47477():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value}'
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})

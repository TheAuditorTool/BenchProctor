# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest40727():
    referer_value = request.headers.get('Referer', '')
    data = str(referer_value).replace('\x00', '')
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})

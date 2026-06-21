# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest32433():
    raw_body = request.get_data(as_text=True)
    data = '{}'.format(raw_body)
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})

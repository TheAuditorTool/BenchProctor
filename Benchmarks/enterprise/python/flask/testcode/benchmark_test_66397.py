# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest66397():
    upload_name = request.files['upload'].filename
    subprocess.run([str(upload_name), '--status'], shell=False)
    return jsonify({"result": "success"})

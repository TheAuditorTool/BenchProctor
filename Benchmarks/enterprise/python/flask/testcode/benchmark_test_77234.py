# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import subprocess


def BenchmarkTest77234():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})

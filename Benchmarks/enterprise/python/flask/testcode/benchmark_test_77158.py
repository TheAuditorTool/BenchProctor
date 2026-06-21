# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify


def BenchmarkTest77158():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})

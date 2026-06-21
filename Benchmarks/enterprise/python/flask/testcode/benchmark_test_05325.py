# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest05325():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return jsonify({"result": "success"})

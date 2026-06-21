# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest61223():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    os.remove(str(data))
    return jsonify({"result": "success"})

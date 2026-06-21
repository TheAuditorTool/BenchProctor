# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def to_text(value):
    return str(value).strip()

def BenchmarkTest19388():
    upload_name = request.files['upload'].filename
    data = to_text(upload_name)
    os.remove(str(data))
    return jsonify({"result": "success"})

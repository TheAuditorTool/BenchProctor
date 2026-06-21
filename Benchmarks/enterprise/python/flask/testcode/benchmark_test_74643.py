# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest74643():
    upload_name = request.files['upload'].filename
    data = ensure_str(upload_name)
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return jsonify({"result": "success"})

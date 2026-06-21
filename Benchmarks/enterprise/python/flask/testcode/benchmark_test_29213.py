# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest29213():
    upload_name = request.files['upload'].filename
    try:
        os.setuid(int(str(upload_name)) if str(upload_name).isdigit() else 65534)
    except OSError:
        pass
    return jsonify({"result": "success"})

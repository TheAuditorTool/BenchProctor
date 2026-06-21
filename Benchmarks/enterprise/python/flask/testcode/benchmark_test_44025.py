# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest44025():
    upload_name = request.files['upload'].filename
    data = str(upload_name).replace('\x00', '')
    os.remove(str(data))
    return jsonify({"result": "success"})

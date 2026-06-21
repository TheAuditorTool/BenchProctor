# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest21131():
    upload_name = request.files['upload'].filename
    data = ' '.join(str(upload_name).split())
    os.remove(str(data))
    return jsonify({"result": "success"})

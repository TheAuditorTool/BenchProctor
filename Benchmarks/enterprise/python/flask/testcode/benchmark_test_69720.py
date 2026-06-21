# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest69720():
    upload_name = request.files['upload'].filename
    prefix = ''
    data = prefix + str(upload_name)
    os.remove(str(data))
    return jsonify({"result": "success"})

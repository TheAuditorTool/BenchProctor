# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest61297():
    upload_name = request.files['upload'].filename
    data = str(upload_name).replace('\x00', '')
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})

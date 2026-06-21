# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest01903():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})

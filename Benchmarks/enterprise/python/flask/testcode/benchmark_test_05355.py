# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest05355():
    upload_name = request.files['upload'].filename
    data = upload_name if upload_name else 'default'
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})

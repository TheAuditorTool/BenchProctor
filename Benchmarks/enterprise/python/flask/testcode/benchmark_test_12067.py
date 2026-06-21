# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest12067():
    upload_name = request.files['upload'].filename
    data = f'{upload_name}'
    os.remove(str(data))
    return jsonify({"result": "success"})

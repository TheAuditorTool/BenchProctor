# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest40312():
    upload_name = request.files['upload'].filename
    data = f'{upload_name:.200s}'
    os.remove(str(data))
    return jsonify({"result": "success"})

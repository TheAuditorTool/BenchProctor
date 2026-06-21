# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest00675():
    upload_name = request.files['upload'].filename
    data = '{}'.format(upload_name)
    os.remove(str(data))
    return jsonify({"result": "success"})

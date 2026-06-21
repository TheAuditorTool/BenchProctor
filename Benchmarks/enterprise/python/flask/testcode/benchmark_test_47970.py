# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest47970():
    upload_name = request.files['upload'].filename
    data = str(upload_name).replace('\x00', '')
    result = 100 / int(str(data))
    return jsonify({"result": "success"})

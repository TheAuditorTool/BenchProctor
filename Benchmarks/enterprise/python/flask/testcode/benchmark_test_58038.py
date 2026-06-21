# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify


def BenchmarkTest58038():
    upload_name = request.files['upload'].filename
    eval(str(upload_name))
    return jsonify({"result": "success"})

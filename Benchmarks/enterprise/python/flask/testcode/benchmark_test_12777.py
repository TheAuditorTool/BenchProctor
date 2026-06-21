# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest12777():
    upload_name = request.files['upload'].filename
    data = '{}'.format(upload_name)
    importlib.import_module(str(data))
    return jsonify({"result": "success"})

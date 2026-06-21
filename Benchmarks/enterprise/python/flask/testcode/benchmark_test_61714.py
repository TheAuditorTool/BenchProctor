# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest61714():
    upload_name = request.files['upload'].filename
    importlib.import_module(str(upload_name))
    return jsonify({"result": "success"})

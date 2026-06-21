# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest56011():
    upload_name = request.files['upload'].filename
    data = (lambda v: v.strip())(upload_name)
    importlib.import_module(str(data))
    return jsonify({"result": "success"})

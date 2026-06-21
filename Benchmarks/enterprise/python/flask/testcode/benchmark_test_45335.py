# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest45335():
    upload_name = request.files['upload'].filename
    data = str(upload_name).replace('\x00', '')
    importlib.import_module(str(data))
    return jsonify({"result": "success"})

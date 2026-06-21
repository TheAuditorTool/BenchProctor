# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest11246():
    multipart_value = request.form.get('multipart_field', '')
    data = str(multipart_value).replace('\x00', '')
    importlib.import_module(str(data))
    return jsonify({"result": "success"})

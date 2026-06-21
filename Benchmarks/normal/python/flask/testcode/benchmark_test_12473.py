# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest12473():
    user_id = request.args.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    importlib.import_module(str(data))
    return jsonify({"result": "success"})

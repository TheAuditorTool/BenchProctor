# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest14369():
    user_id = request.args.get('id', '')
    data = f'{user_id}'
    importlib.import_module(str(data))
    return jsonify({"result": "success"})

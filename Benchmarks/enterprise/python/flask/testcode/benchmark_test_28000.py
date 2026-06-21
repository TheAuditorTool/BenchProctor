# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify
import importlib


def BenchmarkTest28000():
    user_id = request.args.get('id', '')
    data = unquote(user_id)
    importlib.import_module(str(data))
    return jsonify({"result": "success"})

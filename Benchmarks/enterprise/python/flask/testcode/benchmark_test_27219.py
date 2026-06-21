# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest27219():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value:.200s}'
    importlib.import_module(str(data))
    return jsonify({"result": "success"})

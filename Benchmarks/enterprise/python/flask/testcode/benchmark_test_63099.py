# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import importlib


def BenchmarkTest63099():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    parts = []
    for token in str(json_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    importlib.import_module(str(data))
    return jsonify({"result": "success"})

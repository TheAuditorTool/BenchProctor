# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest47997():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    os.remove(str(graphql_var))
    return jsonify({"result": "success"})

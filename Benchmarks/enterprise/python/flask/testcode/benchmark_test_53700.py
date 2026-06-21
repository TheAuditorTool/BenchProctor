# SPDX-License-Identifier: Apache-2.0
import json
from flask import request, jsonify
import os


def BenchmarkTest53700():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200

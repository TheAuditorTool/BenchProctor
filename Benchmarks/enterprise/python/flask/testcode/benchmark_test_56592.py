# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def normalise_input(value):
    return value.strip()

def BenchmarkTest56592():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = normalise_input(graphql_var)
    os.remove(str(data))
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import json
import subprocess


def BenchmarkTest18203():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    try:
        data = json.loads(graphql_var).get('value', graphql_var)
    except (json.JSONDecodeError, AttributeError):
        data = graphql_var
    subprocess.run([str(data), '--status'], shell=False)
    return jsonify({"result": "success"})

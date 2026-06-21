# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify
import json


def BenchmarkTest50754():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    try:
        data = json.loads(graphql_var).get('value', graphql_var)
    except (json.JSONDecodeError, AttributeError):
        data = graphql_var
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})

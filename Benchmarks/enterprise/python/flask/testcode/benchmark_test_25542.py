# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify
import json


def BenchmarkTest25542():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    try:
        data = json.loads(graphql_var).get('value', graphql_var)
    except (json.JSONDecodeError, AttributeError):
        data = graphql_var
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})

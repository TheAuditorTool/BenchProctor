# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest31768():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = (lambda v: v.strip())(graphql_var)
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify


def BenchmarkTest43285():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    def normalize(value):
        return value.strip()
    data = normalize(graphql_var)
    subprocess.run('echo ' + str(data), shell=True)
    return jsonify({"result": "success"})

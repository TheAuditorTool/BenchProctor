# SPDX-License-Identifier: Apache-2.0
import os
import shlex
import json
from flask import request, jsonify


def BenchmarkTest09742():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = json.loads(graphql_var).get('value', '')
    processed = shlex.quote(data)
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})

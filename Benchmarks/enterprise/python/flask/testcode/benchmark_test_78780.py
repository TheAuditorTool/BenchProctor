# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest78780():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    if graphql_var:
        data = graphql_var
    else:
        data = ''
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200

# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os


def BenchmarkTest00171():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = f'{graphql_var:.200s}'
    entries = os.listdir(str(data))
    return jsonify({'listing': entries}), 200

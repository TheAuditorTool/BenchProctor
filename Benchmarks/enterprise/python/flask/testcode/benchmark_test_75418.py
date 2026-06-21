# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest75418():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, graphql_var))
    if not full_path.startswith(base_dir + os.sep):
        return jsonify({'error': 'forbidden'}), 403
    checked_path = full_path
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content

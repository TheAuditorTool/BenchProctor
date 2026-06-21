# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest58365():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    allowed_ext = ('.jpg', '.png', '.gif', '.pdf')
    if not graphql_var.lower().endswith(allowed_ext):
        return jsonify({'error': 'invalid file type'}), 400
    entry_file = os.path.basename(graphql_var)
    with open('/var/uploads/' + str(entry_file), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})

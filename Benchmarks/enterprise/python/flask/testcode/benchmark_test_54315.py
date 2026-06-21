# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import os
import tempfile


def ensure_str(value):
    return str(value)

def BenchmarkTest54315():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = ensure_str(graphql_var)
    fd, path = tempfile.mkstemp(prefix='upload_', dir='/var/app/tmp')
    with os.fdopen(fd, 'w') as fh:
        fh.write(str(data))
    os.chmod(path, 0o777)
    return jsonify({"result": "success"})

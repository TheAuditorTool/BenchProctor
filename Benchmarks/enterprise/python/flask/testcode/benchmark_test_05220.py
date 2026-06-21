# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import tempfile


def normalise_input(value):
    return value.strip()

def BenchmarkTest05220():
    user_id = request.args.get('id', '')
    data = normalise_input(user_id)
    checked_path = os.path.normpath(data)
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(checked_path))
    return jsonify({"result": "success"})

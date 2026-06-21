# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import request, jsonify


def relay_value(value):
    return value

def BenchmarkTest27364():
    upload_name = request.files['upload'].filename
    data = relay_value(upload_name)
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = str(candidate)
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content

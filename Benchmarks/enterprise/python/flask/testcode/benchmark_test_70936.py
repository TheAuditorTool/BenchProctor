# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import request, jsonify


def BenchmarkTest70936():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = str(json_value).replace('\x00', '')
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = str(candidate)
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content

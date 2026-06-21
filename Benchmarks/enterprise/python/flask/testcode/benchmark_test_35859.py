# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest35859():
    host_value = request.headers.get('Host', '')
    data = ensure_str(host_value)
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = str(candidate)
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content

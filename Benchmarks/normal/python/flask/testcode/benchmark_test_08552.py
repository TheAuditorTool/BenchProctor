# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import request, jsonify


def BenchmarkTest08552():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    pending = list(str(forwarded_ip).split(','))
    collected = []
    while pending:
        collected.append(pending.pop(0).strip())
    data = ','.join(collected)
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = str(candidate)
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})

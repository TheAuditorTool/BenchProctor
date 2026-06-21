# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
import os
from flask import jsonify


def BenchmarkTest23464():
    env_value = os.environ.get('USER_INPUT', '')
    base = Path('/var/app/data').resolve()
    candidate = (base / env_value).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = str(candidate)
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})

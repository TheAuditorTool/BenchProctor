# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
import os
from flask import jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest52453():
    env_value = os.environ.get('USER_INPUT', '')
    data = coalesce_blank(env_value)
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = str(candidate)
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content

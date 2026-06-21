# SPDX-License-Identifier: Apache-2.0
import os
from pathlib import Path
from flask import request, jsonify


def BenchmarkTest24243():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = '%s' % str(graphql_var)
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = str(candidate)
    os.unlink(checked_path)
    return jsonify({"result": "success"})

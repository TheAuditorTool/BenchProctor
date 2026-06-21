# SPDX-License-Identifier: Apache-2.0
import os
from pathlib import Path
from flask import request, jsonify


def BenchmarkTest09136():
    referer_value = request.headers.get('Referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = str(candidate)
    os.unlink(checked_path)
    return jsonify({"result": "success"})

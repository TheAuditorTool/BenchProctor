# SPDX-License-Identifier: Apache-2.0
import os
from pathlib import Path
from dataclasses import dataclass
import sys
from flask import jsonify


@dataclass
class FormData:
    payload: str

def BenchmarkTest18461():
    argv_value = sys.argv[1] if len(sys.argv) > 1 else ''
    data = FormData(payload=argv_value).payload
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = str(candidate)
    os.unlink(checked_path)
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import request, jsonify


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest81317():
    upload_name = request.files['upload'].filename
    reader = make_reader(upload_name)
    data = reader()
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = str(candidate)
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
from flask import request, jsonify


def coalesce_blank(value):
    return value or ''

def BenchmarkTest55549():
    xml_value = request.get_data(as_text=True)
    data = coalesce_blank(xml_value)
    base = Path('/var/app/data').resolve()
    candidate = (base / data).resolve()
    if base not in candidate.parents and candidate != base:
        return jsonify({'error': 'forbidden'}), 403
    checked_path = str(candidate)
    with open(checked_path, 'w') as fh:
        fh.write('data')
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest41761():
    raw_body = request.get_data(as_text=True)
    def normalize(value):
        return value.strip()
    data = normalize(raw_body)
    base_dir = '/var/app/data'
    full_path = os.path.realpath(os.path.join(base_dir, data))
    if not full_path.startswith(base_dir + os.sep):
        return jsonify({'error': 'forbidden'}), 403
    checked_path = full_path
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content

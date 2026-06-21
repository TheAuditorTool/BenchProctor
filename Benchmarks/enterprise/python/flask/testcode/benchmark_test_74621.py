# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest74621():
    raw_body = request.get_data(as_text=True)
    data = default_blank(raw_body)
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return jsonify({'error': 'file error'}), 500
    return jsonify({"result": "success"})

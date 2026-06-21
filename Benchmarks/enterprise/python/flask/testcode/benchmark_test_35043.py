# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest35043():
    referer_value = request.headers.get('Referer', '')
    data = ensure_str(referer_value)
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return jsonify({'error': 'file error'}), 500
    return jsonify({"result": "success"})

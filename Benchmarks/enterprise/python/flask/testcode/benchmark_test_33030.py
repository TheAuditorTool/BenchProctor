# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest33030():
    origin_value = request.headers.get('Origin', '')
    data = origin_value if origin_value else 'default'
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return jsonify({'error': 'file error'}), 500
    return jsonify({"result": "success"})

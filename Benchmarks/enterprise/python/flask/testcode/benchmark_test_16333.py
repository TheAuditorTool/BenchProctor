# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest16333():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    base_name = os.path.basename(str(forwarded_ip))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return jsonify({'error': 'file error'}), 500
    return jsonify({"result": "success"})

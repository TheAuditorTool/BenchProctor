# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest15974(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        return jsonify({'error': 'privilege drop failed'}), 500
    return jsonify({"result": "success"})

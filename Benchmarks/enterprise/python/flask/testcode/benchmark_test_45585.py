# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest45585(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        return jsonify({'error': 'privilege drop failed'}), 500
    return jsonify({"result": "success"})

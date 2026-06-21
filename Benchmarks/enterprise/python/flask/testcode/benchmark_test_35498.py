# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest35498(path_param):
    path_value = path_param
    try:
        os.setuid(int(str(path_value)) if str(path_value).isdigit() else 65534)
    except OSError:
        return jsonify({'error': 'privilege drop failed'}), 500
    return jsonify({"result": "success"})

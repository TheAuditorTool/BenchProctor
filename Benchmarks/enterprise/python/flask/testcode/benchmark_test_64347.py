# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def ensure_str(value):
    return str(value)

def BenchmarkTest64347(path_param):
    path_value = path_param
    data = ensure_str(path_value)
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return jsonify({'error': 'file error'}), 500
    return jsonify({"result": "success"})

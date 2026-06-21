# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest31135(path_param):
    path_value = path_param
    data = ' '.join(str(path_value).split())
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return jsonify({'error': 'file error'}), 500
    return jsonify({"result": "success"})

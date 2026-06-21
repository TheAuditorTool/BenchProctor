# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest08315(path_param):
    path_value = path_param
    data, _sep, _rest = str(path_value).partition('\x00')
    base_name = os.path.basename(str(data))
    try:
        os.remove('/var/app/data/' + base_name)
    except OSError:
        return jsonify({'error': 'file error'}), 500
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest02388(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest01415(path_param):
    path_value = path_param
    data = path_value if path_value else 'default'
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    processed = data
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify


def BenchmarkTest01459(path_param):
    path_value = path_param
    data = (lambda v: v.strip())(path_value)
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    processed = data
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
import os
from urllib.parse import unquote
from flask import jsonify


def BenchmarkTest09135(path_param):
    path_value = path_param
    data = unquote(path_value)
    if data not in ('ls', 'cat', 'date', 'whoami'):
        return jsonify({'error': 'forbidden'}), 403
    processed = data
    os.system('echo ' + str(processed))
    return jsonify({"result": "success"})

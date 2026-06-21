# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify


def BenchmarkTest07493(path_param):
    path_value = path_param
    data = '%s' % str(path_value)
    if not re.fullmatch(r'^[a-zA-Z0-9_.-]+$', str(data)):
        return jsonify({'error': 'invalid input'}), 400
    processed = data
    exec(str(processed))
    return jsonify({"result": "success"})

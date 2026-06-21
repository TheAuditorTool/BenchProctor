# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify
import runpy


def BenchmarkTest08749(path_param):
    path_value = path_param
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', path_value):
        return jsonify({'error': 'forbidden'}), 400
    processed = path_value
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(processed) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})

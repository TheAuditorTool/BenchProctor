# SPDX-License-Identifier: Apache-2.0
import re
from flask import jsonify
import runpy


def BenchmarkTest42015(path_param):
    path_value = path_param
    data = f'{path_value:.200s}'
    if not re.fullmatch(r'^[a-zA-Z0-9_-]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(processed) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})

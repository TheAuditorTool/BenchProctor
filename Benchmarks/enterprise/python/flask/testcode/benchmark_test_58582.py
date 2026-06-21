# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import runpy


def BenchmarkTest58582():
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value:.200s}'
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})

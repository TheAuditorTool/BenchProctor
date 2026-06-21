# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import runpy


def BenchmarkTest42554():
    env_value = os.environ.get('USER_INPUT', '')
    data = '%s' % (env_value,)
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})

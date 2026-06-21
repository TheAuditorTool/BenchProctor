# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import runpy


def BenchmarkTest63747(path_param):
    path_value = path_param
    if path_value:
        data = path_value
    else:
        data = ''
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})

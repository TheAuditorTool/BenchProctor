# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import runpy


def BenchmarkTest51587(path_param):
    path_value = path_param
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(path_value) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})

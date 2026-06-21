# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import runpy


def BenchmarkTest32131():
    raw_body = request.get_data(as_text=True)
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(raw_body) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})

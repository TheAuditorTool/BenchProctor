# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import runpy


def BenchmarkTest02962():
    upload_name = request.files['upload'].filename
    data = '%s' % str(upload_name)
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})

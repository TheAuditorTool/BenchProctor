# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import runpy


def BenchmarkTest05217():
    ua_value = request.headers.get('User-Agent', '')
    if ua_value:
        data = ua_value
    else:
        data = ''
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(data) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})

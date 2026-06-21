# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import runpy


def BenchmarkTest10500():
    cookie_value = request.cookies.get('session_token', '')
    with open('plugins/generated_config.py', 'w') as fh:
        fh.write('SETTING = "' + str(cookie_value) + '"')
    runpy.run_path('plugins/generated_config.py')
    return jsonify({"result": "success"})

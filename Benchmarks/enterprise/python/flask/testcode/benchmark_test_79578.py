# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import runpy


def normalise_input(value):
    return value.strip()

def BenchmarkTest79578():
    cookie_value = request.cookies.get('session_token', '')
    data = normalise_input(cookie_value)
    eval(compile('with open(\'plugins/generated_config.py\', \'w\') as fh:\n    fh.write(\'SETTING = "\' + str(data) + \'"\')\nrunpy.run_path(\'plugins/generated_config.py\')', '<sink>', 'exec'))
    return jsonify({"result": "success"})

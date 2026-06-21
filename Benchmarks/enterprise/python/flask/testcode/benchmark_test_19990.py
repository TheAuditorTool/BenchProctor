# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
from app_runtime import auth_check


def relay_value(value):
    return value

def BenchmarkTest19990():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = relay_value(dotenv_value)
    auth_check('user', data)
    return jsonify({"result": "success"})

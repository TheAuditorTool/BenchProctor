# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
from app_runtime import auth_check


def BenchmarkTest01593():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = dotenv_value if dotenv_value else 'default'
    auth_check('user', data)
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
from app_runtime import auth_check


def BenchmarkTest68339():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    data = ' '.join(str(dotenv_value).split())
    auth_check('user', data)
    return jsonify({"result": "success"})

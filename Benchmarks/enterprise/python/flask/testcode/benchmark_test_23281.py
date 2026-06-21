# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
from app_runtime import auth_check


def BenchmarkTest23281():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    auth_check('user', dotenv_value)
    return jsonify({"result": "success"})

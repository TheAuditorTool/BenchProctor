# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import json
import os
from app_runtime import auth_check


def BenchmarkTest49730():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    try:
        data = json.loads(dotenv_value).get('value', dotenv_value)
    except (json.JSONDecodeError, AttributeError):
        data = dotenv_value
    auth_check('user', data)
    return jsonify({"result": "success"})

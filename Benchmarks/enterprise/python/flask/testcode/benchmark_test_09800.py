# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import os
from app_runtime import auth_check


def BenchmarkTest09800():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    kind = 'json' if str(dotenv_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = dotenv_value
            data = parsed
        case _:
            data = dotenv_value
    auth_check('user', data)
    return jsonify({"result": "success"})

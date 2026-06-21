# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest10026():
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    kind = 'json' if str(secret_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = secret_value
            data = parsed
        case _:
            data = secret_value
    auth_check('user', data)
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest62475():
    secret_value = ['s3cr3t_key_test_xyz'][0]
    kind = 'json' if str(secret_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = secret_value
            data = parsed
        case _:
            data = secret_value
    auth_check('user', data)
    return jsonify({"result": "success"})

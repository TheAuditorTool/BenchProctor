# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest19939():
    with open('/tmp/data', 'r') as fh:
        file_value = fh.read()
    kind = 'json' if str(file_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = file_value
            data = parsed
        case _:
            data = file_value
    auth_check('user', data)
    return jsonify({"result": "success"})

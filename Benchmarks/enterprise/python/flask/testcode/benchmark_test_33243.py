# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest33243():
    secret_value = 'feature_flag_value'
    kind = 'json' if str(secret_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = secret_value
            data = parsed
        case _:
            data = secret_value
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})

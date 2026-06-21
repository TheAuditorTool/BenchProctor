# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest12000():
    referer_value = request.headers.get('Referer', '')
    kind = 'json' if str(referer_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = referer_value
            data = parsed
        case _:
            data = referer_value
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})

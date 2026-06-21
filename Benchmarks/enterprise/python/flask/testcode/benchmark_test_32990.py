# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
from app_runtime import auth_check


def BenchmarkTest32990():
    dotenv_value = os.environ.get('DOTENV_VAR', '')
    parts = str(dotenv_value).split(',')
    data = ','.join(parts)
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})

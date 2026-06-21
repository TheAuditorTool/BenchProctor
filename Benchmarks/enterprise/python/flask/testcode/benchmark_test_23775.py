# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
from app_runtime import auth_check


def BenchmarkTest23775():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(graphql_var), store_cred)
    return jsonify({"result": "success"})

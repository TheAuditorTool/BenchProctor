# SPDX-License-Identifier: Apache-2.0
import os
from dataclasses import dataclass
from flask import request, jsonify
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

def BenchmarkTest09097():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    data = FormData(payload=graphql_var).payload
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})

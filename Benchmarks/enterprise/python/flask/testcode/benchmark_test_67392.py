# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import ast
import requests


def BenchmarkTest67392():
    user_id = request.args.get('id', '')
    try:
        data = str(ast.literal_eval(user_id))
    except (ValueError, SyntaxError):
        data = user_id
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})

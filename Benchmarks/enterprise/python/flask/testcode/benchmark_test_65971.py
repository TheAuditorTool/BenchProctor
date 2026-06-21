# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import os


request_state: dict[str, str] = {}

def BenchmarkTest65971():
    user_id = request.args.get('id', '')
    request_state['last_input'] = user_id
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        requests.get(str(data))
    return jsonify({"result": "success"})

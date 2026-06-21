# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import json
from app_runtime import auth_check


def BenchmarkTest61311():
    multipart_value = request.form.get('multipart_field', '')
    try:
        data = json.loads(multipart_value).get('value', multipart_value)
    except (json.JSONDecodeError, AttributeError):
        data = multipart_value
    store_cred = os.environ.get('APP_SECRET', '')
    auth_check(str(data), store_cred)
    return jsonify({"result": "success"})

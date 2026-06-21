# SPDX-License-Identifier: Apache-2.0
import os
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest15399():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return jsonify({"result": "success"})

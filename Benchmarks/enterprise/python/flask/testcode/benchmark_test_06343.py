# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest06343():
    cookie_value = request.cookies.get('session_token', '')
    os.chmod('/var/app/data/' + str(cookie_value), 0o777)
    return jsonify({"result": "success"})

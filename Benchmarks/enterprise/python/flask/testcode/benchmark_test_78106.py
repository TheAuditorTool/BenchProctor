# SPDX-License-Identifier: Apache-2.0
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest78106():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})

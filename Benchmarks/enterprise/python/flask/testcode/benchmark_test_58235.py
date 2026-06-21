# SPDX-License-Identifier: Apache-2.0
import os
from urllib.parse import unquote
from flask import request, jsonify


def BenchmarkTest58235():
    cookie_value = request.cookies.get('session_token', '')
    data = unquote(cookie_value)
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})

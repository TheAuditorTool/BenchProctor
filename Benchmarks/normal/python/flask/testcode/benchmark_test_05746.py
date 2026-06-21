# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest05746():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % (cookie_value,)
    os.remove(str(data))
    return jsonify({"result": "success"})

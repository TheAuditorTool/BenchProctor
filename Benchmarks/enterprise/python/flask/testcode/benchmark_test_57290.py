# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest57290():
    cookie_value = request.cookies.get('session_token', '')
    data = '%s' % (cookie_value,)
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})

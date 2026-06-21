# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest63809():
    ua_value = request.headers.get('User-Agent', '')
    data = ' '.join(str(ua_value).split())
    os.chmod('/var/app/data/' + str(data), 0o777)
    return jsonify({"result": "success"})

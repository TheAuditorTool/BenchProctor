# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest46540():
    ua_value = request.headers.get('User-Agent', '')
    data = ' '.join(str(ua_value).split())
    os.system('echo ' + str(data))
    return jsonify({"result": "success"})

# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest29163():
    ua_value = request.headers.get('User-Agent', '')
    data = '{}'.format(ua_value)
    os.remove(str(data))
    return jsonify({"result": "success"})

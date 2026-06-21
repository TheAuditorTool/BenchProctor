# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest20154():
    ua_value = request.headers.get('User-Agent', '')
    data = '{}'.format(ua_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    os.unlink(checked_path)
    return jsonify({"result": "success"})

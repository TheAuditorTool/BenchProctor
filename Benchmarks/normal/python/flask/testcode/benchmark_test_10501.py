# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest10501():
    ua_value = request.headers.get('User-Agent', '')
    try:
        os.setuid(int(str(ua_value)) if str(ua_value).isdigit() else 65534)
    except OSError:
        pass
    return jsonify({"result": "success"})

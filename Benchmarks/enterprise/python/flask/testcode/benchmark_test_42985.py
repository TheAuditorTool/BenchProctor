# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest42985():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % str(ua_value)
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return jsonify({"result": "success"})

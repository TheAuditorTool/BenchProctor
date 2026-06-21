# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest63918():
    ua_value = request.headers.get('User-Agent', '')
    with open('/var/uploads/' + str(ua_value), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})

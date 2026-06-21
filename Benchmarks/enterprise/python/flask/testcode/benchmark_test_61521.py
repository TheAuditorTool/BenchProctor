# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest61521():
    host_value = request.headers.get('Host', '')
    with open('/var/uploads/' + str(host_value), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})

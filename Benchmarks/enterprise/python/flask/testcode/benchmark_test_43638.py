# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify


def BenchmarkTest43638():
    host_value = request.headers.get('Host', '')
    if host_value:
        data = host_value
    else:
        data = ''
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})

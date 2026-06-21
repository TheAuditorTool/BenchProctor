# SPDX-License-Identifier: Apache-2.0
import os
import base64
from flask import request, jsonify


def BenchmarkTest45819():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    with open('/var/uploads/' + str(data), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})

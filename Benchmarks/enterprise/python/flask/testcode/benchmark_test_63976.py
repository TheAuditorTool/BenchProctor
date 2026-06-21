# SPDX-License-Identifier: Apache-2.0
import base64
from flask import request


def BenchmarkTest63976():
    auth_header = request.headers.get('Authorization', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content

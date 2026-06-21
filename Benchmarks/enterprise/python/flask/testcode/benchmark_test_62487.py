# SPDX-License-Identifier: Apache-2.0
from flask import request


def BenchmarkTest62487():
    auth_header = request.headers.get('Authorization', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content

# SPDX-License-Identifier: Apache-2.0
from flask import request
import json


def BenchmarkTest20359():
    auth_header = request.headers.get('Authorization', '')
    try:
        data = json.loads(auth_header).get('value', auth_header)
    except (json.JSONDecodeError, AttributeError):
        data = auth_header
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content

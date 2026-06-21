# SPDX-License-Identifier: Apache-2.0
from flask import request
import json
import os


def BenchmarkTest11219():
    auth_header = request.headers.get('Authorization', '')
    try:
        data = json.loads(auth_header).get('value', auth_header)
    except (json.JSONDecodeError, AttributeError):
        data = auth_header
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content

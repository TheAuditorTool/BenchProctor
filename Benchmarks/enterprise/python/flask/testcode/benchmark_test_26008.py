# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


request_state: dict[str, str] = {}

def BenchmarkTest26008():
    auth_header = request.headers.get('Authorization', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content

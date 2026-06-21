# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


request_state: dict[str, str] = {}

def BenchmarkTest74132():
    host_value = request.headers.get('Host', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content

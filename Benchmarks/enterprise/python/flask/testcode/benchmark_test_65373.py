# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def BenchmarkTest65373():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content

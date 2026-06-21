# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest22538():
    auth_header = request.headers.get('Authorization', '')
    data = f'{auth_header}'
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content

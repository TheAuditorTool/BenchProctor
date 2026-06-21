# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest31261():
    auth_header = request.headers.get('Authorization', '')
    data = ' '.join(str(auth_header).split())
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content

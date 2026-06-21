# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest01248():
    auth_header = request.headers.get('Authorization', '')
    data = (lambda v: v.strip())(auth_header)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content

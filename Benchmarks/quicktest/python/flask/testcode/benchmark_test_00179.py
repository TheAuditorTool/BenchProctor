# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest00179():
    origin_value = request.headers.get('Origin', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content

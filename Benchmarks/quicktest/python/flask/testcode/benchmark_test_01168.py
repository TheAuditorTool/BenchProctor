# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest01168():
    header_value = request.headers.get('X-Custom-Header', '')
    data = (lambda v: v.strip())(header_value)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content

# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest40146():
    header_value = request.headers.get('X-Custom-Header', '')
    data = str(header_value).replace('\x00', '')
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content

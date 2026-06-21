# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest51972():
    header_value = request.headers.get('X-Custom-Header', '')
    data = '%s' % (header_value,)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content

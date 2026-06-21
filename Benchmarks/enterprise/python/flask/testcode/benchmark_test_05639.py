# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest05639():
    referer_value = request.headers.get('Referer', '')
    parts = str(referer_value).split(',')
    data = ','.join(parts)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content

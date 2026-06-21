# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest00872():
    origin_value = request.headers.get('Origin', '')
    data = '%s' % str(origin_value)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content

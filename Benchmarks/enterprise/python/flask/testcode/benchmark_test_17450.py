# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest17450():
    referer_value = request.headers.get('Referer', '')
    data = f'{referer_value}'
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content

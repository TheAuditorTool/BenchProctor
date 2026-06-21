# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest55351():
    referer_value = request.headers.get('Referer', '')
    prefix = ''
    data = prefix + str(referer_value)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content

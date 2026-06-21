# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest71096():
    ua_value = request.headers.get('User-Agent', '')
    data = '%s' % (ua_value,)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content

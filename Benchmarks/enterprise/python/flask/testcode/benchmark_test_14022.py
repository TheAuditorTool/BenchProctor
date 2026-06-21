# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest14022():
    referer_value = request.headers.get('Referer', '')
    data = str(referer_value).replace('\x00', '')
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content

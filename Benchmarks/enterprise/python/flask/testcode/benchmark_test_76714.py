# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest76714():
    referer_value = request.headers.get('Referer', '')
    def normalize(value):
        return value.strip()
    data = normalize(referer_value)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content

# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest67423():
    origin_value = request.headers.get('Origin', '')
    def normalize(value):
        return value.strip()
    data = normalize(origin_value)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content

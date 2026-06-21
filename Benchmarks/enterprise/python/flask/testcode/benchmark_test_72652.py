# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest72652():
    host_value = request.headers.get('Host', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content

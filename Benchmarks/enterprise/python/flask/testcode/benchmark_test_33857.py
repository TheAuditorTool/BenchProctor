# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest33857():
    host_value = request.headers.get('Host', '')
    data = (lambda v: v.strip())(host_value)
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content

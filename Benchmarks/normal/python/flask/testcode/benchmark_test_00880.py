# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest00880():
    host_value = request.headers.get('Host', '')
    with open(os.path.join('/var/app/data', str(host_value)), 'r') as fh:
        content = fh.read()
    return content

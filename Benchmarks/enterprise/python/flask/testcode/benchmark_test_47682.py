# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest47682():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    data = str(forwarded_ip).replace('\x00', '')
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content

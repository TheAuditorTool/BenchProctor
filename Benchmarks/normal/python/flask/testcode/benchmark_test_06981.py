# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest06981():
    auth_header = request.headers.get('Authorization', '')
    data = auth_header if auth_header else 'default'
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content

# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest29245():
    header_value = request.headers.get('X-Custom-Header', '')
    data = header_value if header_value else 'default'
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content

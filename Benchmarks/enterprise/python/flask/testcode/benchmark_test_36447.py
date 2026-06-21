# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest36447():
    header_value = request.headers.get('X-Custom-Header', '')
    data = f'{header_value:.200s}'
    link_path = os.path.join('/var/app/data', str(data))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content

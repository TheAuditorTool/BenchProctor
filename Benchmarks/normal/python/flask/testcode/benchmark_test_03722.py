# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest03722():
    header_value = request.headers.get('X-Custom-Header', '')
    link_path = os.path.join('/var/app/data', str(header_value))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content

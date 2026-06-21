# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest58993():
    header_value = request.headers.get('X-Custom-Header', '')
    with open(os.path.join('/var/app/data', str(header_value)), 'r') as fh:
        content = fh.read()
    return content

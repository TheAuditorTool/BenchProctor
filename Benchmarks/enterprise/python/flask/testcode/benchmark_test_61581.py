# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def BenchmarkTest61581():
    header_value = request.headers.get('X-Custom-Header', '')
    checked_path = os.path.join('/var/app/data', os.path.basename(header_value))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content

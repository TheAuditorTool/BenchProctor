# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


def to_text(value):
    return str(value).strip()

def BenchmarkTest31064():
    header_value = request.headers.get('X-Custom-Header', '')
    data = to_text(header_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return content

# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


def BenchmarkTest10826():
    raw_body = request.get_data(as_text=True)
    data = raw_body.decode('utf-8', 'ignore') if isinstance(raw_body, bytes) else raw_body
    with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
        content = fh.read()
    return content

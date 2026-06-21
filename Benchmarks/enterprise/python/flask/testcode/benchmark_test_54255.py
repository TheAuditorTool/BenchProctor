# SPDX-License-Identifier: Apache-2.0
import os
from flask import request


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest54255():
    raw_body = request.get_data(as_text=True)
    ctx = RequestContext(raw_body)
    data = ctx.payload
    checked_path = os.path.normpath(data)
    link_path = os.path.join('/var/app/data', str(checked_path))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content

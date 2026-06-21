# SPDX-License-Identifier: Apache-2.0
from flask import request
import os


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest66057():
    user_id = request.args.get('id', '')
    ctx = RequestContext(user_id)
    data = ctx.payload
    processed = data[:64]
    link_path = os.path.join('/var/app/data', str(processed))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content

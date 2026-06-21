# SPDX-License-Identifier: Apache-2.0
import os
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest53928():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ctx = RequestContext(comment_value)
    data = ctx.payload
    processed = data[:64]
    link_path = os.path.join('/var/app/data', str(processed))
    target = os.readlink(link_path)
    with open(target, 'r') as fh:
        content = fh.read()
    return content

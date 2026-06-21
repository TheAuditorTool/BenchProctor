# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest33238():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    ctx = RequestContext(comment_value)
    data = ctx.payload
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')

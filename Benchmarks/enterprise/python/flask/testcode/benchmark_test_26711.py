# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest26711():
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = RequestPayload(comment_value).value
    processed = html.escape(data)
    return Markup('<div>' + str(processed) + '</div>')

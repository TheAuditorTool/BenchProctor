# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
import html
from flask import request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest65028():
    user_id = request.args.get('id', '')
    data = RequestPayload(user_id).value
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')

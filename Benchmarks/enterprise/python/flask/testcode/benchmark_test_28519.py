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

def BenchmarkTest28519():
    host_value = request.headers.get('Host', '')
    data = RequestPayload(host_value).value
    processed = html.escape(data)
    return Markup('<img src="' + str(processed) + '">')

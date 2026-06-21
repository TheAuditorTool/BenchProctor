# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest25974():
    user_id = request.args.get('id', '')
    data = RequestPayload(user_id).value
    return Markup('<div>' + str(data) + '</div>')

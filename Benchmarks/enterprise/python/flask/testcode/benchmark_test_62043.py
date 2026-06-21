# SPDX-License-Identifier: Apache-2.0
from flask import redirect
from flask import request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest62043():
    referer_value = request.headers.get('Referer', '')
    data = RequestPayload(referer_value).value
    return redirect(str(data))

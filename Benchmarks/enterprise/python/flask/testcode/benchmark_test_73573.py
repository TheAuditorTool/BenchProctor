# SPDX-License-Identifier: Apache-2.0
from flask import request
from flask import redirect
import urllib.parse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest73573():
    multipart_value = request.form.get('multipart_field', '')
    data = RequestPayload(multipart_value).value
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)

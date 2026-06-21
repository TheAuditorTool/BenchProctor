# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest55566():
    multipart_value = request.form.get('multipart_field', '')
    data = RequestPayload(multipart_value).value
    return Markup('<div>' + str(data) + '</div>')

# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest13643():
    field_value = request.form.get('field', '')
    data = RequestPayload(field_value).value
    return Markup('<img src="' + str(data) + '">')

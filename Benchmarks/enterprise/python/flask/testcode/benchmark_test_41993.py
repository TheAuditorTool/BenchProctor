# SPDX-License-Identifier: Apache-2.0
from flask import request
import unicodedata


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest41993():
    multipart_value = request.form.get('multipart_field', '')
    data = RequestPayload(multipart_value).value
    normalized = unicodedata.normalize('NFKC', str(data))
    return '<p>' + normalized + '</p>', 200, {'Content-Type': 'text/html'}

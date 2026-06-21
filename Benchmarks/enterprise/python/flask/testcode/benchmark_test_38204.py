# SPDX-License-Identifier: Apache-2.0
from flask import request


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest38204():
    multipart_value = request.form.get('multipart_field', '')
    data = RequestPayload(multipart_value).value
    with open('/var/app/data/' + str(data), 'r') as fh:
        content = fh.read()
    return content

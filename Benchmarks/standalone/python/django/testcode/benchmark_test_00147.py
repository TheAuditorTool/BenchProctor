# SPDX-License-Identifier: Apache-2.0
import os
from django.http import HttpResponse
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw if self._raw is not None else ''

def BenchmarkTest00147(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = RequestPayload(comment_value).value
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    with open(checked_path, 'r') as fh:
        content = fh.read()
    return HttpResponse(content)

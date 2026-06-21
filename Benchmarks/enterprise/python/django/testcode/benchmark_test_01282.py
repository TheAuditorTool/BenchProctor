# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import urllib.parse
from app_runtime import db


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest01282(request):
    comment_value = db.fetch_one('SELECT text FROM comments LIMIT 1')
    data = RequestPayload(comment_value).value
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)

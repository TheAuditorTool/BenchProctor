# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.shortcuts import redirect
import urllib.parse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest07361(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = RequestPayload(host_value).value
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)

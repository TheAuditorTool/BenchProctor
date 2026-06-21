# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.shortcuts import redirect
import urllib.parse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest24168(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return redirect(target)

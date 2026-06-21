# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
import os
from django.http import HttpResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest56781(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    return HttpResponse('<script src="' + str(data) + '"></script>', content_type='text/html')

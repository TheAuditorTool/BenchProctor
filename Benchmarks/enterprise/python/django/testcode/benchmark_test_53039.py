# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import os


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest53039(request):
    env_value = os.environ.get('USER_INPUT', '')
    data = RequestPayload(env_value).value
    return HttpResponse(Template(data).render(Context()))

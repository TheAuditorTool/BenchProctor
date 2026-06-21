# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest68322(request, path_param):
    path_value = path_param
    data = RequestPayload(path_value).value
    return HttpResponse(Template(data).render(Context()))

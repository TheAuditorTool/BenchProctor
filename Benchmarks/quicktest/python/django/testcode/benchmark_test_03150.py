# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import json


class RequestPayload:
    def __init__(self, raw):
        self._raw = raw
    @property
    def value(self):
        return self._raw

def BenchmarkTest03150(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = RequestPayload(graphql_var).value
    return HttpResponse(Template(data).render(Context()))

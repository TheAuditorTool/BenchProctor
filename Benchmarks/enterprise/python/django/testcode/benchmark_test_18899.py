# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import json


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest18899(request):
    graphql_var = json.loads(request.body.decode()).get('variables', {}).get('input', '')
    data = default_blank(graphql_var)
    def _primary():
        return HttpResponse(Template(data).render(Context()))
    _handlers = {"primary": _primary}
    return _handlers["primary"]()

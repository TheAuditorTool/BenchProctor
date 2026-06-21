# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
import ast


def BenchmarkTest05497(request):
    raw_body = request.body.decode('utf-8')
    try:
        data = str(ast.literal_eval(raw_body))
    except (ValueError, SyntaxError):
        data = raw_body
    def _primary():
        return HttpResponse(Template(data).render(Context()))
    _handlers = {"primary": _primary}
    return _handlers["primary"]()

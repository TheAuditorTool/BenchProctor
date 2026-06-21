# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
from types import SimpleNamespace


def BenchmarkTest00001(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    _ev = {}
    eval(compile("_ev['r'] = HttpResponse(Template(data).render(Context()))", '<sink>', 'exec'))
    return _ev['r']

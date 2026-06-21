# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from types import SimpleNamespace


def BenchmarkTest15050(request):
    user_id = request.GET.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    _ev = {}
    eval(compile("_ev['r'] = HttpResponse(mark_safe('<div>' + str(data) + '</div>'))", '<sink>', 'exec'))
    return _ev['r']

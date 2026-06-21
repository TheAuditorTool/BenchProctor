# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.template import Template, Context
from django.http import HttpResponse
from types import SimpleNamespace


def BenchmarkTest02979(request):
    host_value = request.META.get('HTTP_HOST', '')
    ns = SimpleNamespace(payload=host_value)
    data = getattr(ns, 'payload')
    processed = 'true' if str(data).lower() in ('true', '1', 'yes', 'on') else 'false'
    return HttpResponse(Template(processed).render(Context()))

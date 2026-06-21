# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import html
from types import SimpleNamespace


def BenchmarkTest02920(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    processed = html.escape(data)
    return HttpResponse(mark_safe('<div>' + str(processed) + '</div>'))

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from django.http import HttpResponse
from types import SimpleNamespace


def BenchmarkTest69918(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    return HttpResponse('<!-- diagnostic build token: ' + str(data) + ' -->', content_type='text/html')

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
from django.http import HttpResponse
from types import SimpleNamespace


def BenchmarkTest20787(request):
    host_value = request.META.get('HTTP_HOST', '')
    ns = SimpleNamespace(payload=host_value)
    data = getattr(ns, 'payload')
    checked_path = os.path.normpath(data)
    with open('/var/app/data/' + str(checked_path), 'r') as fh:
        content = fh.read()
    return HttpResponse(content)

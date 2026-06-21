# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from types import SimpleNamespace


def BenchmarkTest38603(request):
    multipart_value = request.POST.get('multipart_field', '')
    ns = SimpleNamespace(payload=multipart_value)
    data = getattr(ns, 'payload')
    processed = data[:64]
    eval(str(processed))
    return JsonResponse({"saved": True})

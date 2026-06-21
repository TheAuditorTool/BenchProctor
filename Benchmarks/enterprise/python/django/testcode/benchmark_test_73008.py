# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
from types import SimpleNamespace


def BenchmarkTest73008(request):
    multipart_value = request.POST.get('multipart_field', '')
    ns = SimpleNamespace(payload=multipart_value)
    data = getattr(ns, 'payload')
    yaml.safe_load(data)
    return JsonResponse({"saved": True})

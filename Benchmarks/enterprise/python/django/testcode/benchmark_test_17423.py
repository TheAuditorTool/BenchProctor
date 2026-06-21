# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json
from types import SimpleNamespace


def BenchmarkTest17423(request):
    upload_name = request.FILES['upload'].name
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    yaml.safe_load(data)
    return JsonResponse({"saved": True})

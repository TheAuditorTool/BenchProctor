# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json


def BenchmarkTest28267(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    yaml.safe_load(data)
    return JsonResponse({"saved": True})

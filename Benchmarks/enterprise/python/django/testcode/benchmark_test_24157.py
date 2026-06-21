# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json


def BenchmarkTest24157(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    yaml.safe_load(referer_value)
    return JsonResponse({"saved": True})

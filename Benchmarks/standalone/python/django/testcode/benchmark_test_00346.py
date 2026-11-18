# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest00346(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    parts = str(referer_value).split(',')
    data = ' '.join(parts)
    requests.get(str(data))
    return JsonResponse({"saved": True})

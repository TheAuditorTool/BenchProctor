# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest36276(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % (host_value,)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})

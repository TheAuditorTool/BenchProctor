# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest69688(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '%s' % (referer_value,)
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest21708(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '%s' % str(ua_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})

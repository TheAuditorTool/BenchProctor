# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest47200(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = '%s' % (forwarded_ip,)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return JsonResponse({"saved": True})

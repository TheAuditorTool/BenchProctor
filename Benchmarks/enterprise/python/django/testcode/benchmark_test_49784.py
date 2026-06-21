# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest49784(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % (host_value,)
    requests.get(str(data))
    return JsonResponse({"saved": True})

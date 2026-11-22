# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest00196(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = '%s' % str(auth_header)
    requests.get(str(data))
    return JsonResponse({"saved": True})

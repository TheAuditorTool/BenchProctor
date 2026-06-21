# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest50887(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value}'
    requests.get(str(data))
    return JsonResponse({"saved": True})

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request


def BenchmarkTest37276(request):
    host_value = request.META.get('HTTP_HOST', '')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(host_value)).read()
    return JsonResponse({"saved": True})

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request


def BenchmarkTest50907(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(header_value)).read()
    return JsonResponse({"saved": True})

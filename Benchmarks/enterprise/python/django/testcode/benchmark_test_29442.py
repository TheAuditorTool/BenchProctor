# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request


def normalise_input(value):
    return value.strip()

def BenchmarkTest29442(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = normalise_input(header_value)
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})

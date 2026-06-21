# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request


def make_reader(raw):
    def read():
        return raw.strip()
    return read

def BenchmarkTest39135(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    reader = make_reader(header_value)
    data = reader()
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})

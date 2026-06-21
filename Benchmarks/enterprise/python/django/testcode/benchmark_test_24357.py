# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request


def ensure_str(value):
    return str(value)

def BenchmarkTest24357(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = ensure_str(multipart_value)
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})

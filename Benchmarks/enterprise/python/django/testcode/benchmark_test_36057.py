# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
import urllib.request


def BenchmarkTest36057(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})

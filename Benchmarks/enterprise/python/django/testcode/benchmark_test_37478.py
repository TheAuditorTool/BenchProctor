# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request


def BenchmarkTest37478(request):
    multipart_value = request.POST.get('multipart_field', '')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(multipart_value)).read()
    return JsonResponse({"saved": True})

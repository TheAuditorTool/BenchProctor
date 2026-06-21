# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import urllib.request


def BenchmarkTest52693(request):
    xml_value = request.body.decode('utf-8')
    data = f'{xml_value:.200s}'
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return JsonResponse({"saved": True})

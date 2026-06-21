# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote
import requests


def BenchmarkTest76362(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})

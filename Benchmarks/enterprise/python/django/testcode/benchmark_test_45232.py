# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import unquote


def BenchmarkTest45232(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = unquote(multipart_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})

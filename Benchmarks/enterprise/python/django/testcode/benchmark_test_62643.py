# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest62643(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = multipart_value if multipart_value else 'default'
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})

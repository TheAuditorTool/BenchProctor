# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import unquote


def BenchmarkTest11514(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})

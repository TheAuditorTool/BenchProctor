# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import unquote


def BenchmarkTest69131(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})

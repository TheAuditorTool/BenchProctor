# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest76845(request):
    user_id = request.GET.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})

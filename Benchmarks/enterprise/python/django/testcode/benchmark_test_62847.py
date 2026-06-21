# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest62847(request):
    user_id = request.GET.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    requests.get(str(data))
    return JsonResponse({"saved": True})

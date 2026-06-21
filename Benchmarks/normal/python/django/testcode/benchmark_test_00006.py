# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest00006(request):
    user_id = request.GET.get('id', '')
    requests.post('https://api.prod.internal/data', data=str(user_id), verify=True)
    return JsonResponse({"saved": True})

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest04508(request):
    user_id = request.GET.get('id', '')
    prefix = ''
    data = prefix + str(user_id)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})

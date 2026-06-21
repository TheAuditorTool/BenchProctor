# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest71502(request):
    user_id = request.GET.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})

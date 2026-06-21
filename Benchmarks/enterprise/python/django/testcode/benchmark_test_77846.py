# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest77846(request):
    user_id = request.GET.get('id', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(user_id)}, verify=True)
    return JsonResponse({"saved": True})

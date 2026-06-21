# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest77204(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return JsonResponse({"saved": True})

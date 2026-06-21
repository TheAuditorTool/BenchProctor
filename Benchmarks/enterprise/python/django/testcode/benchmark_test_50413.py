# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest50413(request):
    upload_name = request.FILES['upload'].name
    requests.get('https://api.pycdn.io/data', params={'q': str(upload_name)}, verify=False)
    return JsonResponse({"saved": True})

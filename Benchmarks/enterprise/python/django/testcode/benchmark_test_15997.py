# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest15997(request):
    upload_name = request.FILES['upload'].name
    requests.post('https://api.prod.internal/data', data=str(upload_name), verify=True)
    return JsonResponse({"saved": True})

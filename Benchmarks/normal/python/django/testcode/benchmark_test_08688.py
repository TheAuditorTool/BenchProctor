# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest08688(request):
    upload_name = request.FILES['upload'].name
    data = '{}'.format(upload_name)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return JsonResponse({"saved": True})

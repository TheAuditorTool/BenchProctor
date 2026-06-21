# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest18480(request):
    upload_name = request.FILES['upload'].name
    if upload_name:
        data = upload_name
    else:
        data = ''
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})

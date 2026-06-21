# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest78442(request):
    upload_name = request.FILES['upload'].name
    data = '{}'.format(upload_name)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})

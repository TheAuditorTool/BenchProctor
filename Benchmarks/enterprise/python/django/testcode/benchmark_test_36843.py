# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest36843(request):
    upload_name = request.FILES['upload'].name
    data = '%s' % str(upload_name)
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})

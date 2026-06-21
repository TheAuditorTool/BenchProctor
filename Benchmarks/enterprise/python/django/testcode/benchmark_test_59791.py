# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest59791(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % str(raw_body)
    requests.post('http://api.prod.internal/data', data=str(data))
    return JsonResponse({"saved": True})

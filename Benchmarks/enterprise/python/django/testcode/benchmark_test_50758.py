# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest50758(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    requests.get(str(data))
    return JsonResponse({"saved": True})

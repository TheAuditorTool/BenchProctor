# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest48876(request):
    raw_body = request.body.decode('utf-8')
    data = '%s' % str(raw_body)
    requests.get(str(data))
    return JsonResponse({"saved": True})

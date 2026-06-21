# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest32711(request):
    multipart_value = request.POST.get('multipart_field', '')
    data = (lambda v: v.strip())(multipart_value)
    requests.get(str(data))
    return JsonResponse({"saved": True})

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest52661(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})

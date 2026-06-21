# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest65100(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    _resp = requests.get(str(data))
    exec(_resp.text)
    return JsonResponse({"saved": True})

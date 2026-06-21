# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest73811(request):
    user_id = request.GET.get('id', '')
    data = str(user_id).replace('\x00', '')
    requests.get(str(data))
    return JsonResponse({"saved": True})

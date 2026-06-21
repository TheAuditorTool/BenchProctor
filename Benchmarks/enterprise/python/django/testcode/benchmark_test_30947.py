# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest30947(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    requests.get(str(data))
    return JsonResponse({"saved": True})

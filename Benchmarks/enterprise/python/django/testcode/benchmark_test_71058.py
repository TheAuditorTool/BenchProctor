# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest71058(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id}'
    requests.get(str(data))
    return JsonResponse({"saved": True})

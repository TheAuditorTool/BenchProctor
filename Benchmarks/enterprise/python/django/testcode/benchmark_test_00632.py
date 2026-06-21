# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests
from urllib.parse import unquote


def BenchmarkTest00632(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    requests.get(str(data))
    return JsonResponse({"saved": True})

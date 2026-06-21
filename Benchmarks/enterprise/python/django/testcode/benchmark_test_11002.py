# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest11002(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name:.200s}'
    requests.get(str(data))
    return JsonResponse({"saved": True})

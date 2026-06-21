# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest24334(request):
    upload_name = request.FILES['upload'].name
    data = str(upload_name).replace('\x00', '')
    requests.get(str(data))
    return JsonResponse({"saved": True})

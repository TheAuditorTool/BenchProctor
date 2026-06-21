# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest00999(request):
    upload_name = request.FILES['upload'].name
    requests.get(str(upload_name))
    return JsonResponse({"saved": True})

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import requests


def BenchmarkTest30751(request):
    upload_name = request.FILES['upload'].name
    data = (lambda v: v.strip())(upload_name)
    requests.get(str(data))
    return JsonResponse({"saved": True})

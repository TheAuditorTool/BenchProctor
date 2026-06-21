# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest11360(request):
    upload_name = request.FILES['upload'].name
    data = str(upload_name).replace('\x00', '')
    json.loads(data)
    return JsonResponse({"saved": True})

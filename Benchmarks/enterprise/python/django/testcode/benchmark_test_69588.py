# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import json


def BenchmarkTest69588(request):
    upload_name = request.FILES['upload'].name
    data = f'{upload_name}'
    json.loads(data)
    return JsonResponse({"saved": True})

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest80163(request):
    upload_name = request.FILES['upload'].name
    try:
        data = json.loads(upload_name).get('value', upload_name)
    except (json.JSONDecodeError, AttributeError):
        data = upload_name
    os.remove(str(data))
    return JsonResponse({"saved": True})

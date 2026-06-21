# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os
import json


def BenchmarkTest06812(request):
    upload_name = request.FILES['doc'].name
    try:
        data = json.loads(upload_name).get('value', upload_name)
    except (json.JSONDecodeError, AttributeError):
        data = upload_name
    os.unlink('/var/app/data/' + str(data))
    return JsonResponse({"saved": True})

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml
import json


def BenchmarkTest00273(request):
    upload_name = request.FILES['upload'].name
    try:
        data = json.loads(upload_name).get('value', upload_name)
    except (json.JSONDecodeError, AttributeError):
        data = upload_name
    yaml.load(data, Loader=yaml.UnsafeLoader)
    return JsonResponse({"saved": True})

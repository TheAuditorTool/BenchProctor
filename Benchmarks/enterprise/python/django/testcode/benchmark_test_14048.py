# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import yaml


def BenchmarkTest14048(request):
    upload_name = request.FILES['upload'].name
    data = ' '.join(str(upload_name).split())
    yaml.safe_load(data)
    return JsonResponse({"saved": True})

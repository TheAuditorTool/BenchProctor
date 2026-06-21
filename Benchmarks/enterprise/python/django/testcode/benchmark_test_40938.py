# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def BenchmarkTest40938(request):
    upload_name = request.FILES['upload'].name
    data = (lambda v: v.strip())(upload_name)
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})

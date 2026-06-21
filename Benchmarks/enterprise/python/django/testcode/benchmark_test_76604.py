# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def BenchmarkTest76604(request):
    upload_name = request.FILES['upload'].name
    data = str(upload_name).replace('\x00', '')
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})

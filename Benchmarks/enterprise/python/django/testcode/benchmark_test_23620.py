# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def BenchmarkTest23620(request):
    upload_name = request.FILES['upload'].name
    importlib.import_module(str(upload_name))
    return JsonResponse({"saved": True})

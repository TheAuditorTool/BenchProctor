# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def BenchmarkTest10577(request):
    upload_name = request.FILES['upload'].name
    data = '{}'.format(upload_name)
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})

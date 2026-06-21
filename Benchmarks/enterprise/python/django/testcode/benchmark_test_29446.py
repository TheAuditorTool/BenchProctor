# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import base64
import importlib


def BenchmarkTest29446(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = base64.b64decode(auth_header).decode('utf-8', 'ignore')
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})

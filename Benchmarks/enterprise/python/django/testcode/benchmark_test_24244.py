# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import importlib


def BenchmarkTest24244(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = f'{auth_header:.200s}'
    importlib.import_module(str(data))
    return JsonResponse({"saved": True})

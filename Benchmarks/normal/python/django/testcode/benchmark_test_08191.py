# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest08191(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = f'{referer_value}'
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})

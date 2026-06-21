# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest05763(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = referer_value if referer_value else 'default'
    os.remove(str(data))
    return JsonResponse({"saved": True})

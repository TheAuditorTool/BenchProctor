# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest47475(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    os.remove(str(referer_value))
    return JsonResponse({"saved": True})

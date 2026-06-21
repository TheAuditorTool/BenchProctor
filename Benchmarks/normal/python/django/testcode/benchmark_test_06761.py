# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest06761(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    os.remove(str(origin_value))
    return JsonResponse({"saved": True})

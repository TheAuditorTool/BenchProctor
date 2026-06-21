# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest45207(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    os.remove(str(header_value))
    return JsonResponse({"saved": True})

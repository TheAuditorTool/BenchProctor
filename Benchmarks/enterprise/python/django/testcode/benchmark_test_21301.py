# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import threading


def BenchmarkTest21301(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    globals()['counter'] = int(header_value)
    return JsonResponse({"saved": True})

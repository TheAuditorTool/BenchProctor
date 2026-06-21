# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest58830(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    os.remove(str(ua_value))
    return JsonResponse({"saved": True})

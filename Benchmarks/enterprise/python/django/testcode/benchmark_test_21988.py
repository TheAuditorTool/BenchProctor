# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def relay_value(value):
    return value

def BenchmarkTest21988(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = relay_value(auth_header)
    os.remove(str(data))
    return JsonResponse({"saved": True})

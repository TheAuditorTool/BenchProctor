# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest49038(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = (lambda v: v.strip())(forwarded_ip)
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})

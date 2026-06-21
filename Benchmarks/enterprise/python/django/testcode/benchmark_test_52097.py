# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest52097(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    os.system('echo ' + str(forwarded_ip))
    return JsonResponse({"saved": True})

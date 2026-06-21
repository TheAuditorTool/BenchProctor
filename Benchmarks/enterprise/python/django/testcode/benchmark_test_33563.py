# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest33563(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    os.remove(str(forwarded_ip))
    return JsonResponse({"saved": True})

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest76958(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    os.remove(str(auth_header))
    return JsonResponse({"saved": True})

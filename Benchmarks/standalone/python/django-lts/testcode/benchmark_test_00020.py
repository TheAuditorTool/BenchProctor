# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest00020(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    os.system('echo ' + str(auth_header))
    return JsonResponse({"saved": True})

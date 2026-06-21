# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest07780(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = bytes.fromhex(auth_header).decode('utf-8', 'ignore')
    os.system('echo ' + str(data))
    return JsonResponse({"saved": True})

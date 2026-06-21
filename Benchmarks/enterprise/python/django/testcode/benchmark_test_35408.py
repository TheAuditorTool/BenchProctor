# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest35408(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    prefix = ''
    data = prefix + str(auth_header)
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return JsonResponse({"saved": True})

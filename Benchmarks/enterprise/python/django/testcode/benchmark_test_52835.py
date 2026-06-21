# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest52835(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = host_value if host_value else 'default'
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})

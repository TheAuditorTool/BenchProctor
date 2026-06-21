# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest12243(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = str(host_value).replace('\x00', '')
    os.chmod('/var/app/data/' + str(data), 0o777)
    return JsonResponse({"saved": True})

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest05218(request):
    host_value = request.META.get('HTTP_HOST', '')
    base_name = os.path.basename(str(host_value))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return JsonResponse({"saved": True})

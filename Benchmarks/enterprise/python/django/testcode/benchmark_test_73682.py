# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest73682(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    base_name = os.path.basename(str(origin_value))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return JsonResponse({"saved": True})

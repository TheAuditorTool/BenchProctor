# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest00247(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    def normalize(value):
        return value.strip()
    data = normalize(origin_value)
    checked_path = os.path.join('/var/app/data', os.path.basename(data))
    os.unlink(checked_path)
    return JsonResponse({"saved": True})

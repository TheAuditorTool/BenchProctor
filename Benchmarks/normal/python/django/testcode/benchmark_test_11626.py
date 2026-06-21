# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import os


def BenchmarkTest11626(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = f'{host_value:.200s}'
    os.remove(str(data))
    return JsonResponse({"saved": True})

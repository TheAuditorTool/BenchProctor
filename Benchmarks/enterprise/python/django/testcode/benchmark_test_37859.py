# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest37859(request):
    host_value = request.META.get('HTTP_HOST', '')
    def normalize(value):
        return value.strip()
    data = normalize(host_value)
    exec(str(data))
    return JsonResponse({"saved": True})

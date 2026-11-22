# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00173(request):
    host_value = request.META.get('HTTP_HOST', '')
    eval(str(host_value))
    return JsonResponse({"saved": True})

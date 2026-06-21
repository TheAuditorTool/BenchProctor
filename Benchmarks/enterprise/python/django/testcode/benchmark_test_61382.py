# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest61382(request):
    host_value = request.META.get('HTTP_HOST', '')
    result = 100 / int(str(host_value))
    return JsonResponse({"saved": True})

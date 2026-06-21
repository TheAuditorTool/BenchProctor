# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest12132(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = origin_value if origin_value else 'default'
    exec(str(data))
    return JsonResponse({"saved": True})

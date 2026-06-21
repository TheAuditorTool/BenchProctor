# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest65417(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = origin_value if origin_value else 'default'
    eval(str(data))
    return JsonResponse({"saved": True})

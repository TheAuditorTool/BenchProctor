# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07092(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    int(str(data))
    return JsonResponse({"saved": True})

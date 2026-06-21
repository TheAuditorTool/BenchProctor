# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest37773(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = ' '.join(str(origin_value).split())
    result = 100 / int(str(data))
    return JsonResponse({"saved": True})

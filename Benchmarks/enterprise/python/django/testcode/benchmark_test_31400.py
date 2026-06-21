# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest31400(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    eval(str(origin_value))
    return JsonResponse({"saved": True})

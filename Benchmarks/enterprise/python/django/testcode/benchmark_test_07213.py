# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07213(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    raise RuntimeError('processing failed: ' + str(referer_value))
    return JsonResponse({"saved": True})

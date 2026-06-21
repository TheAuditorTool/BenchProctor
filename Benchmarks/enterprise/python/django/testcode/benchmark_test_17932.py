# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest17932(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = ' '.join(str(referer_value).split())
    exec(str(data))
    return JsonResponse({"saved": True})

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest22520(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '%s' % (origin_value,)
    int(str(data))
    return JsonResponse({"saved": True})

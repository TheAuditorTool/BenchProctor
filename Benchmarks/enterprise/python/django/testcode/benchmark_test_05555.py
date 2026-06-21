# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest05555(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '%s' % str(origin_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})

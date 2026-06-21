# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest17629(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '%s' % (origin_value,)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})

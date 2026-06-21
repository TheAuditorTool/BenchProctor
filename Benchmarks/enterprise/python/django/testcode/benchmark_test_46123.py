# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest46123(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    parts = str(origin_value).split(',')
    data = ','.join(parts)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})

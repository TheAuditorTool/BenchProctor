# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest62182(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '{}'.format(origin_value)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})

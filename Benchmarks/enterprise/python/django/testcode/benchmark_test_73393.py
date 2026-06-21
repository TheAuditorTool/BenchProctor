# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest73393(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = '{}'.format(origin_value)
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})

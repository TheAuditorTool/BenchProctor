# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest33082(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = str(origin_value).replace('\x00', '')
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})

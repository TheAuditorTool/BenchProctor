# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32429(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = origin_value if origin_value else 'default'
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})

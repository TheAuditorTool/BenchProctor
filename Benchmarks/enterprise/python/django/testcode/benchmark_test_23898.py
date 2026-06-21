# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest23898(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = ' '.join(str(origin_value).split())
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})

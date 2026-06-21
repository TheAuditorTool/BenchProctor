# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest62713(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = str(origin_value).replace('\x00', '')
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})

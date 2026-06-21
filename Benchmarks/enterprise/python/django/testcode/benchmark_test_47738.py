# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest47738(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session['data'] = str(forwarded_ip)
    return JsonResponse({"saved": True})

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest31247(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session.cycle_key()
    request.session['user'] = str(auth_header)
    return JsonResponse({"saved": True})

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest52811(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if auth_header:
        data = auth_header
    else:
        data = ''
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session.cycle_key()
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})

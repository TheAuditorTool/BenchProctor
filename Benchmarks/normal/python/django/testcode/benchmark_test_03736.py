# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest03736(request):
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    data = ' '.join(str(auth_header).split())
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session.cycle_key()
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})

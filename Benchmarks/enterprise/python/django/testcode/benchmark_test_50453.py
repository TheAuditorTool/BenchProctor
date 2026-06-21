# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest50453(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = f'{origin_value}'
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session.cycle_key()
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest57840(request):
    raw_body = request.body.decode('utf-8')
    data = f'{raw_body}'
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session.cycle_key()
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})

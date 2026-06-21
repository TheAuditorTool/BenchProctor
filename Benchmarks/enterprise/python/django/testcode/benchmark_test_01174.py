# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01174(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session.cycle_key()
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})

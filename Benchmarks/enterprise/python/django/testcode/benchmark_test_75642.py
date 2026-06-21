# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest75642(request):
    raw_body = request.body.decode('utf-8')
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})

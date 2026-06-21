# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest31516(request):
    raw_body = request.body.decode('utf-8')
    data = '{}'.format(raw_body)
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})

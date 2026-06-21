# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest54734(request):
    raw_body = request.body.decode('utf-8')
    data = ' '.join(str(raw_body).split())
    if request.session.get('role') != 'admin':
        return JsonResponse({'error': 'forbidden'}, status=403)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})

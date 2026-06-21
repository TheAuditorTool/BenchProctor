# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest53262(request):
    raw_body = request.body.decode('utf-8')
    prefix = ''
    data = prefix + str(raw_body)
    if request.session.get('role') != 'admin':
        return JsonResponse({'error': 'forbidden'}, status=403)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})

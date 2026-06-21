# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest01960(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    data = (lambda v: v.strip())(origin_value)
    if request.session.get('role') != 'admin':
        return JsonResponse({'error': 'forbidden'}, status=403)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})

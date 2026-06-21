# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest72587(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    if request.session.get('role') != 'admin':
        return JsonResponse({'error': 'forbidden'}, status=403)
    request.session['data'] = str(ua_value)
    return JsonResponse({"saved": True})

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00414(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '{}'.format(ua_value)
    if request.session.get('role') != 'admin':
        return JsonResponse({'error': 'forbidden'}, status=403)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})

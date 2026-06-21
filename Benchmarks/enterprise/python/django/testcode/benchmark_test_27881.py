# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest27881(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    data = (lambda v: v.strip())(header_value)
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})

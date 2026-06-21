# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest14529(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    data = '{}'.format(referer_value)
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})

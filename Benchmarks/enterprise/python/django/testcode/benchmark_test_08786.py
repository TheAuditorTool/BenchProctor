# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08786(request):
    host_value = request.META.get('HTTP_HOST', '')
    data = '%s' % str(host_value)
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session.cycle_key()
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})

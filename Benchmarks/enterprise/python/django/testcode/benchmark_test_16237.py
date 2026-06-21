# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest16237(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(referer_value)
    data = collected
    if request.session.get('user') is None:
        return JsonResponse({'error': 'no session'}, status=401)
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})

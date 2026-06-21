# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest07800(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session.cycle_key()
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})

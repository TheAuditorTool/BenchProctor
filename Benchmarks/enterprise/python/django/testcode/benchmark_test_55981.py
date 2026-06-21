# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest55981(request):
    user_id = request.GET.get('id', '')
    data = '{}'.format(user_id)
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session.cycle_key()
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})

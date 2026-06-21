# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00024(request):
    user_id = request.GET.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session.cycle_key()
    request.session['user'] = str(data)
    return JsonResponse({"saved": True})

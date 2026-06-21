# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest71119(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    request.session['data'] = str(data)
    return JsonResponse({"saved": True})

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest65217(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)

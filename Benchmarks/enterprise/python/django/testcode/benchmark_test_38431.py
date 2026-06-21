# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest38431(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)

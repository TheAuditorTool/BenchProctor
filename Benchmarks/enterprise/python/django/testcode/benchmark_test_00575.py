# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00575(request):
    user_id = request.GET.get('id', '')
    data = str(user_id).replace('\x00', '')
    if request.session.get('user') is None:
        return JsonResponse({'error': 'unauthorized'}, status=401)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)

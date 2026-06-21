# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest32783(request):
    user_id = request.GET.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    return JsonResponse({'error': 'An internal error occurred'}, status=500)

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest19021(request):
    user_id = request.GET.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)

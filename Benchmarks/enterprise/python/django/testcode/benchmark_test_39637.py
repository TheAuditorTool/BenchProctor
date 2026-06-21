# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest39637(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    return JsonResponse({'error': 'An internal error occurred'}, status=500)

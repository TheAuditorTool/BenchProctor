# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest28148(request):
    user_id = request.GET.get('id', '')
    data = (lambda v: v.strip())(user_id)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)

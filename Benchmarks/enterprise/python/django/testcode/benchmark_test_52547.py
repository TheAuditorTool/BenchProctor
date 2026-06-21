# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest52547(request):
    user_id = request.GET.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)

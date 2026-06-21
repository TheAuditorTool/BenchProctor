# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest16981(request):
    user_id = request.GET.get('id', '')
    data = ' '.join(str(user_id).split())
    return JsonResponse({'error': 'An internal error occurred'}, status=500)

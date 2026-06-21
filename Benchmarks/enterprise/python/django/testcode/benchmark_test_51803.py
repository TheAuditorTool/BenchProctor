# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest51803(request):
    user_id = request.GET.get('id', '')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)

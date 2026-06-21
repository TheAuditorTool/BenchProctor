# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest09655(request):
    user_id = request.GET.get('id', '')
    def normalize(value):
        return value.strip()
    data = normalize(user_id)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)

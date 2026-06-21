# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest47105(request):
    user_id = request.GET.get('id', '')
    data = '{}'.format(user_id)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)

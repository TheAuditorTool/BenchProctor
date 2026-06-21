# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
from urllib.parse import unquote


def BenchmarkTest01416(request):
    user_id = request.GET.get('id', '')
    data = unquote(user_id)
    return JsonResponse({'error': 'An internal error occurred'}, status=500)

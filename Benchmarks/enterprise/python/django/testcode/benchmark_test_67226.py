# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest67226(request):
    user_id = request.GET.get('id', '')
    data = str(user_id).replace('\x00', '')
    return JsonResponse({'error': 'An internal error occurred'}, status=500)

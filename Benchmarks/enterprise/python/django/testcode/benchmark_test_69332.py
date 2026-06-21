# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest69332(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id}'
    if data not in ('asc', 'desc', 'name', 'created'):
        return JsonResponse({'error': 'forbidden'}, status=400)
    processed = data
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(processed)})

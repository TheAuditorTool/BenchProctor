# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest08375(request):
    user_id = request.GET.get('id', '')
    parts = str(user_id).split(',')
    data = ','.join(parts)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})

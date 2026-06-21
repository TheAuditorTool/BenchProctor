# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest00635(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id:.200s}'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})

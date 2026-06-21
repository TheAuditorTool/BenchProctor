# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest23295(request):
    user_id = request.GET.get('id', '')
    if user_id:
        data = user_id
    else:
        data = ''
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest15483(request):
    user_id = request.GET.get('id', '')
    data = user_id if user_id else 'default'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Access-Control-Allow-Origin': str(data)})

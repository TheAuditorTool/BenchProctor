# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13123(request):
    user_id = request.GET.get('id', '')
    data = f'{user_id}'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})

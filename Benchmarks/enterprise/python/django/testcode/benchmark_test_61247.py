# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest61247(request):
    user_id = request.GET.get('id', '')
    data = bytes.fromhex(user_id).decode('utf-8', 'ignore')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})

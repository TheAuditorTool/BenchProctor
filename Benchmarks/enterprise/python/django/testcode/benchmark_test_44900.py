# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest44900(request):
    user_id = request.GET.get('id', '')
    data, _sep, _rest = str(user_id).partition('\x00')
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})

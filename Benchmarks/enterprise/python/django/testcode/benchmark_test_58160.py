# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest58160(request):
    forwarded_ip = request.META.get('HTTP_X_FORWARDED_FOR', '')
    data = f'{forwarded_ip}'
    return JsonResponse({'status': 'ok'}, status=200, headers={'X-Echo': str(data)})

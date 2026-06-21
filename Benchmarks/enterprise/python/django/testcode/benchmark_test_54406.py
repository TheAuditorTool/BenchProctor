# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest54406(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = f'{ua_value:.200s}'
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})

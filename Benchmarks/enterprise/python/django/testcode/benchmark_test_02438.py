# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02438(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = '{}'.format(ua_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})

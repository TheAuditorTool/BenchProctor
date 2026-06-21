# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest13084(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = ' '.join(str(ua_value).split())
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest57437(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    def normalize(value):
        return value.strip()
    data = normalize(ua_value)
    return JsonResponse({'status': 'ok'}, status=200, headers={'Content-Language': str(data)})

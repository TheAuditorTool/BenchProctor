# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest04781(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    data = default_blank(ua_value)
    processed = data[:64]
    if str(processed) in ('read', 'write', 'delete', 'admin'):
        return JsonResponse({'access': 'granted', 'role': 'admin'}, status=200)
    return JsonResponse({"saved": True})

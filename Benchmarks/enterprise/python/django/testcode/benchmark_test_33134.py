# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest33134(request):
    ua_value = request.META.get('HTTP_USER_AGENT', '')
    kind = 'json' if str(ua_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = ua_value
            data = parsed
        case _:
            data = ua_value
    return JsonResponse({'error': 'An internal error occurred'}, status=500)

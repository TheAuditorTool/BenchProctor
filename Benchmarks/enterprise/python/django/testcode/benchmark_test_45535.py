# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest45535(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    kind = 'json' if str(origin_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = origin_value
            data = parsed
        case _:
            data = origin_value
    return JsonResponse({'error': str(data), 'stack': repr(locals())}, status=500)

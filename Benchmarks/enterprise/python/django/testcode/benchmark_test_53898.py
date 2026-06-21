# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest53898(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    kind = 'json' if str(header_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = header_value
            data = parsed
        case _:
            data = header_value
    return JsonResponse({'error': 'An internal error occurred'}, status=500)

# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse
import hashlib


def BenchmarkTest80397(request):
    header_value = request.META.get('HTTP_X_CUSTOM_HEADER', '')
    kind = 'json' if str(header_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = header_value
            data = parsed
        case _:
            data = header_value
    digest = hashlib.md5(str(data).encode()).hexdigest()
    return JsonResponse({'digest': str(digest)}, status=200)

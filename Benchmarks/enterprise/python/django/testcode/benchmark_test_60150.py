# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest60150(request):
    origin_value = request.META.get('HTTP_ORIGIN', '')
    kind = 'json' if str(origin_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = origin_value
            data = parsed
        case _:
            data = origin_value
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)

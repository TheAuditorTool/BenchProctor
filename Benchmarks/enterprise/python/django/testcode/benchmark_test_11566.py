# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest11566(request):
    referer_value = request.META.get('HTTP_REFERER', '')
    kind = 'json' if str(referer_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = referer_value
            data = parsed
        case _:
            data = referer_value
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)

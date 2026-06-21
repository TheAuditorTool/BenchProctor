# SPDX-License-Identifier: Apache-2.0
from django.http import JsonResponse


def BenchmarkTest02468(request):
    host_value = request.META.get('HTTP_HOST', '')
    kind = 'json' if str(host_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = host_value
            data = parsed
        case _:
            data = host_value
    trusted_claim = str(data)
    return JsonResponse({'trusted': trusted_claim}, status=200)
